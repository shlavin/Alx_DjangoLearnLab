from django.shortcuts import render

#added
from django_filters import rest_framework as drf_filters
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Book 
from.serializers import BookSerializer

'''
Book List View with filtering , searching and ordering capabilities.
its purpose is to retrieve all books that is get only
its permissions are to allow read-only for everyone

'''
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]

    #DRF built-in filters
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    #Filtering setup
    filterset_fields = ['title', 'author', 'publication_year']

    #searching setup
    search_fields = ['title', 'author__name']

    #ordering setup
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] #default ordering


'''
Book detail view
its purpose is to retrieve a single book by Id(GET)
permissions allowed is read only for everyone
'''
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class= BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


'''
Book create view
its purpose is to create a new book(POST)
its custom behaviour is onluy logged in users can create a new book
'''
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        '''
        custom hook to execute logic  before saving
        also add automated author assignment here its a necessity
        '''
        serializer.save()


'''
Book update view
it updates existing book by id (PUT/PATCH)
its permission is that onlu authenticated users can update
'''

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticated]

    def perform_update(self,serializer):
        '''
         custom hoook to validate or modify data before saving .
        '''
        serializer.save()


'''
Book delete View
it deletes books by ID (DELETE)
its permissions is that only authenticated users can delete
'''

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]





