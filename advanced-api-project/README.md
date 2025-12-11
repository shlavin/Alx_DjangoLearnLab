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
