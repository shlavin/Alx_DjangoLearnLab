from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class TestBookAPI(APITestCase):
    '''
    Tests for:
    CRUD operations
    Permisssions
    Filtering
    Searching
    Ordering
    '''
    def setUp(self):
        #Test client
        self.client = APIClient()

        #Create a user for authenticated requests
        self.user = User.objects.create_user(
            username='kahumu',
            password='password123'
        )

        #Creating authors
        self.author1 = Author.objects.create(name='shlavin kahumu')
        self.author2 = Author.objects.create(name='bransel njenga')

        #Creating books
        self.book1 = Book.objects.create(
            title='The great gabsy',
            publication_year=2012,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title='The Diary of a Wimpy Kid',
            publication_year=2010,
            author=self.author1

        )
        self.book3 = Book.objects.create(
            title='Matilda',
            publication_year=2011,
            author=self.author2

        )


    # LIST VIEW TESTS
    def test_list_books(self):
        '''Ensuring GET/api/books/ returns all books'''
        response = self.client.get('/api/books')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3) 

    # DETAIL VIEW TEST  
    def test_retrieve_book(self):
        '''Ensuring GET/api/books/<id>/ works'''
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Matilda')

    #CREATE VIEW TEST
    def test_create_book_requires_auth(self):
        '''Unauthenticated users cannot create books'''
        data = {
            'title':'The Kahumus',
            'publication_year': 2022,
            'author': self.author1.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Authenticated users CAN create books."""
        self.client.login(username="kahumu", password="password123")

        data = {
            "title": "Created By Test",
            "publication_year": 2021,
            "author": self.author1.id
        }

        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
    
    #UPDATE VIEW TEST
    def test_update_book(self):
        """Authenticated user can update a book."""
        self.client.login(username="kahumu", password="password123")
        data = {"title": "Updated Title"}

        response = self.client.patch(f"/api/books/update/{self.book1.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")
    
    # DELETE VIEW TEST
    def test_delete_book(self):
        """Authenticated user can delete a book."""
        self.client.login(username="kahumu", password="password123")

        response = self.client.delete(f"/api/books/delete/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    #Filtering test
    def test_filter_books_by_author(self):
        """Filter books by author ID."""
        response = self.client.get(f"/api/books/?author={self.author1.id}")
        self.assertEqual(len(response.data), 2)

    def test_filter_books_by_year(self):
        """Filter books by publication_year."""
        response = self.client.get("/api/books/?publication_year=2019")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django Unleashed")

    # SEARCH TEST

    def test_search_books(self):
        """Search books by title or author name."""
        response = self.client.get("/api/books/?search=django")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django Unleashed")

        # ORDERING TESTS
    def test_order_books_title(self):
        """Order by title ascending."""
        response = self.client.get("/api/books/?ordering=title")
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles))

    def test_order_books_publication_year_desc(self):
        """Order by publication_year descending."""
        response = self.client.get("/api/books/?ordering=-publication_year")
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))    