# relationship_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Book, Library, UserProfile


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
# Custom Permission-Protected Book Views
# --------------------------------

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author_id=author)
        messages.success(request, 'Book added successfully!')
        return redirect('list_books')
    return render(request, 'relationship_app/add_book.html')


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author = request.POST.get('author')
        if author:
            book.author_id = author
        book.save()
        messages.success(request, 'Book updated successfully!')
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})


# --------------------------------
# Authentication Views
# --------------------------------

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Ensure UserProfile is created immediately
            UserProfile.objects.get_or_create(user=user, defaults={'role': 'Member'})
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
                messages.error(request, "Invalid username or password.")
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

@user_passes_test(
    lambda u: u.is_authenticated and hasattr(u, 'userprofile') and u.userprofile.role == 'Admin',
    login_url='/login/'
)
def admin_view(request):
    if not (hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'Admin'):
        return HttpResponseForbidden("You are not authorized to view this page.")
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(lambda u: u.is_authenticated and hasattr(u, 'userprofile') and u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(lambda u: u.is_authenticated and hasattr(u, 'userprofile') and u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
