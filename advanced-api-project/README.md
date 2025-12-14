# API View Documentation

This project uses Django REST Framework's generic views to handle CRUD operations.

## Views
- **BookListView** – List all books (GET)
- **BookDetailView** – Retrieve one book by ID (GET)
- **BookCreateView** – Add new book (POST)
- **BookUpdateView** – Modify book (PUT/PATCH)
- **BookDeleteView** – Delete book (DELETE)

## Permissions
- Unauthenticated users: read-only
- Authenticated users: can create, update, delete

## Endpoints
- `/api/books/`
- `/api/books/<id>/`
- `/api/books/create/`
- `/api/books/<id>/update/`
- `/api/books/<id>/delete/`

# Filtering, Searching & Ordering (DRF)

The BookListView supports advanced data querying:

## Filtering
Filter by exact match:
- /api/books/?title=1984
- /api/books/?publication_year=2020
- /api/books/?author=1

## Searching
Search across title and author's name:
- /api/books/?search=python
- /api/books/?search=orwell

## Ordering
Sort results:
- /api/books/?ordering=title
- /api/books/?ordering=-publication_year

These features are enabled using:
- DjangoFilterBackend
- SearchFilter
- OrderingFilter


# Running API Tests

The project includes full unit tests for Book API CRUD operations, filtering,
searching, ordering, and authentication.

Run the tests:

    python manage.py test api

Tests cover:
- Creating books
- Retrieving books
- Updating books
- Deleting books
- Filtering by author & year
- Searching titles/authors
- Ordering results
- Permission controls
