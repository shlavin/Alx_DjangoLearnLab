from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
     """
    Public endpoint to list all books.
    
    Authentication:
        - None required (AllowAny)
        
    Permissions:
        - permissions.AllowAny allows anyone (authenticated or not) to access this endpoint.
        
    Usage:
        GET /api/books/ returns a JSON list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookViewSet(viewsets.ModelViewSet):
     """
    Endpoint for all CRUD operations on Book model.

    Authentication:
        - TokenAuthentication is required for all actions.
        - Users must include the token in the Authorization header:
          Authorization: Token <user_token>
    
    Permissions:
        - IsAuthenticated ensures that only logged-in users with valid tokens
          can perform create, update, or delete operations.
        - Unauthenticated users will receive HTTP 401 Unauthorized.
    
    CRUD Endpoints Provided Automatically:
        - list:    GET    /api/books_all/
        - create:  POST   /api/books_all/
        - retrieve:GET    /api/books_all/<id>/
        - update:  PUT    /api/books_all/<id>/
        - partial_update: PATCH /api/books_all/<id>/
        - destroy: DELETE /api/books_all/<id>/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
