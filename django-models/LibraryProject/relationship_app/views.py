# relationship_app/views.py

from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Book, Library
from .forms import RegisterForm  # Make sure you have forms.py with RegisterForm

# -----------------------------
# Function-Based View — List all books
# -----------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# -----------------------------
# Class-Based View — Show library details
# -----------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# -----------------------------
# Authentication Views
# -----------------------------

# Registration view
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. You can now login.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect("list_books")  # Redirect to a page after login
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Logout view
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return render(request, "relationship_app/logout.html")
