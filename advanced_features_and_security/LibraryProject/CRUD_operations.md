CRUD Operations for the Book Model

This document demonstrates the Create, Retrieve, Update, and Delete operations for the Book model in the bookshelf Django app.
Each operation is executed in the Django shell (python manage.py shell).

 Create Operation

Objective: Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

Python Command:

from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book



# Output:
<Book: 1984 by George Orwell>
# The book instance has been successfully created in the database.
 Retrieve Operation

Objective: Retrieve and display all attributes of the book created in the previous step.

Python Command:

from bookshelf.models import Book
books = Book.objects.all()
for b in books:
    print(b.id, b.title, b.author, b.publication_year)



# Output:
1 1984 George Orwell 1949
# The details of the created book are successfully displayed.
 Update Operation

Objective: Update the title of the created book from “1984” to “Nineteen Eighty-Four”.

Python Command:

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.all()



# Output:
<QuerySet [<Book: Nineteen Eighty-Four by George Orwell>]>
# The book title has been successfully updated.
 Delete Operation

Objective: Delete the created book and confirm the deletion by retrieving all books again.

Python Command:

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()



# Output:
(1, {'bookshelf.Book': 1})
<QuerySet []>
# The book has been successfully deleted and the database is no