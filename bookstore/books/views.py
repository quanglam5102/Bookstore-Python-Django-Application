from atexit import register
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import BookForm
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            print('User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Invalid username or passwors')

    context = {'page': page}
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            print("Error happened during registration")

    return render(request, 'login_register.html', {'form': form})


# View for books
def books(request):
    books = Book.objects.all()

    bookDetails = {
        "page_title": "BookStore",
        "books": books,
    }

    return render(request, "homepage.html", bookDetails)

def book(request, pk):
    book = Book.objects.get(id=pk)
    bookDetails = {
        "page_title": "Book Details",
        "book": book,
    }

    # Render movies template with context
    return render(request, "bookDetails.html", bookDetails)

def queryBook(request):
    if request.method == "POST":
        bookId = request.POST.get("id")
        book = Book.objects.get(id=bookId)
        bookDetails = {
            "page_title": "Book Details",
            "book": book,
        }
        return render(request, "bookDetails.html", bookDetails)
    return render(request, "bookById.html")

@login_required(login_url="login")
def addBook(request):
    form = BookForm()
    if request.method == 'POST':
        Book.objects.create(
            posted_by=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            year=request.POST.get('year'),
            rating=request.POST.get('rating'),
            author=request.POST.get('author'),
        )
        return redirect('/')

    newBook = {'book': form}
    return render(request, 'addBook.html', newBook)


@login_required(login_url="login")
def editBook(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if request.user != book.posted_by:
        return render(request, "not_authorized.html")

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        form.save()

        return redirect('/')
        # book.title = request.POST.get('title')
        # book.author = request.POST.get('author')
        # book.description = request.POST.get('description')
        # book.year = request.POST.get('year')
        # book.rating = request.POST.get('rating')
        # book.save()

        # return redirect('/')

    bookInfo = {'book': form}

    return render(request, 'editBook.html', bookInfo)

@login_required(login_url="login")
def deleteBook(request, pk):
    book = Book.objects.get(id=pk)

    if request.user != book.posted_by:
        return render(request, "not_authorized.html")

    if request.method == 'POST':
        book.delete()
        return redirect('/')

    return render(request, 'deleteBook.html', {'book': book})
