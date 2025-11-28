from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection
from .models import Book
from .forms import BookForm, BookSearchForm  # ensure this form exists


# -------------------------------
# List Books (View permission)
# Access restricted using login + permission decorators
# Prevents unauthorized users from viewing book records
# -------------------------------
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # ORM ensures safe query execution
    return render(request, 'bookshelf/book_list.html', {'books': books})


# -------------------------------
# Create Book (Create permission)
# User input handled via Django forms, which auto-escape output
# CSRF token applied automatically via Django templates
# -------------------------------
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)  # form validation prevents unsafe input
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})


# -------------------------------
# Edit Book (Edit permission)
# Editing is protected from unauthorized access by permission checks
# ORM prevents SQL injection vulnerabilities
# -------------------------------
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():              # prevents invalid/malicious data
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})


# -------------------------------
# Delete Book (Delete permission)
# Protected by login + permission decorators
# Uses ORM delete() which is protected from SQL injection
# -------------------------------
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})


# -------------------------------
# Secure Book Search
# Uses Django ORM filtering to safely handle user-supplied input
# Mitigates SQL injection by avoiding raw SQL queries
# -------------------------------
@login_required
def search_books(request):
    form = BookSearchForm(request.GET)
    books = []
    if form.is_valid():
        query = form.cleaned_data['query']   # cleaned_data prevents malicious input
        books = Book.objects.filter(title__icontains=query)  # ORM safe query
    return render(request, 'bookshelf/search_results.html', {'books': books, 'form': form})


# -------------------------------
# Optional raw SQL search (safe parameterized)
# Query parameters passed using placeholders (%) binding prevents SQL injection
# -------------------------------
def raw_search_books(query):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM bookshelf_book WHERE title LIKE %s",
            [f"%{query}%"]                 # parameterized to prevent SQL injection
        )
        return cursor.fetchall()
