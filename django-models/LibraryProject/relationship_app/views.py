from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Book, Library

# --------------------------------
# Book and Library Views
# --------------------------------

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# --------------------------------
# Authentication Views
# --------------------------------

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created and logged in successfully!")
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

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
                return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return render(request, "relationship_app/logout.html")

# --------------------------------
# Role-Based Access Control (RBAC)
# --------------------------------

def admin(request):
    if not request.user.is_authenticated or not hasattr(request.user, 'userprofile'):
        return HttpResponseForbidden("You are not authorized to access this page.")
    if request.user.userprofile.role != 'Admin':
        return HttpResponseForbidden("You are not authorized to access this page.")
    return render(request, 'relationship_app/admin_view.html')

def librarian_view(request):
    if not request.user.is_authenticated or not hasattr(request.user, 'userprofile'):
        return HttpResponseForbidden("You are not authorized to access this page.")
    if request.user.userprofile.role != 'Librarian':
        return HttpResponseForbidden("You are not authorized to access this page.")
    return render(request, 'relationship_app/librarian_view.html')

def member_view(request):
    if not request.user.is_authenticated or not hasattr(request.user, 'userprofile'):
        return HttpResponseForbidden("You are not authorized to access this page.")
    if request.user.userprofile.role != 'Member':
        return HttpResponseForbidden("You are not authorized to access this page.")
    return render(request, 'relationship_app/member_view.html')
