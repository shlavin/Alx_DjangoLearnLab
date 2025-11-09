import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# ------------------------------
#  Query all books by a specific author
# ------------------------------
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:") 
        if books.exists():
            for book in books:
                print(f"- {book.title}")
        else:
            print(f"No books found for {author_name}.")
            
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'.")



# ------------------------------
#  List all books in a specific library
# ------------------------------
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books available in {library_name} library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")


# ------------------------------
#  Retrieve the librarian for a specific library
# ------------------------------
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  
        print(f"The librarian for {library_name} is {librarian.name}.")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")


# ------------------------------
# Example calls
# ------------------------------
if __name__ == "__main__":
    get_books_by_author("John Doe")
    list_books_in_library("City Library")
    get_librarian_for_library("City Library")
