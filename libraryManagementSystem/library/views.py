from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import BookForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.messages import get_messages

def dashboard(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            return login_view(request)
        elif 'register' in request.POST:
            return register_view(request)
    return render(request, 'library/dashboard.html')

# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'library/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('dashboard')

# Registration View
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "There was an error with your registration. Please try again.")
    else:
        form = UserCreationForm()

    # Clear messages manually if needed
    # This will get all the messages in the current session and mark them as "consumed"
    get_messages(request)

    return render(request, 'library/register.html', {'form': form})


# View All Books
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

# View Specific Book
@login_required
def book_detail(request, book_id):
    # Fetch the book by its ID or return a 404 if not found
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST" and "reserve" in request.POST:
        if book.available:
            book.reserved_by.add(request.user)
            book.available = False
            book.save()
            return redirect('book_detail', book_id=book.id)
    return render(request, 'library/book_detail.html', {'book': book})

# Add Book
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect back to the books list
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

# Edit Book
@login_required
def edit_book(request, book_id):
    # Fetch the book by its ID or return 404 if not found
    book = get_object_or_404(Book, id=book_id)

    # Pre-fill the form with the book's current data
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)  # Redirect to the book detail page
    else:
        form = BookForm(instance=book)

    return render(request, 'library/edit_book.html', {'form': form, 'book': book})

# Delete Book
@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the book list page after deletion

    return render(request, 'library/delete_book.html', {'book': book})

# Reserve Book
# not working
#@login_required
#def reserve_book(request, book_id):
 #   book = get_object_or_404(Book, id=book_id)
 #   book.reserved_by.add(request.user)
 #   return redirect('book_detail', book_id=book.id)