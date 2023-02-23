from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from books.models import Book, Category
from books.forms import BookModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from datetime import date, timedelta
# Create your views here.


def books(request):
    """
    docstring
    """
    categories = Category.objects.all()
    return render(request, 'books/books.html', {'categories': categories})

@login_required(login_url='login')
def viewBook(request, bookID):
    book = get_object_or_404(Book, pk=bookID)
    sameCatBooks = book.category.books.exclude(pk=bookID)
    # timedelta adds days hours, weeks etc
    todayDate = (date.today() + timedelta(1)).strftime('%Y-%m-%d')

    return render(request, 'books/book.html', {"book":book, "cat" :book.category, "catBooks":sameCatBooks, "todayDate":todayDate})

@login_required(login_url='login')
def borrowBook(request, bookID):
    book = get_object_or_404(Book, pk = bookID)
    user = request.user
    student = user.student
    book.return_date = request.GET['return_date']
    book.status = 'f'
    student.books.add(book)
    book.save()
    return redirect('studentBooks')

def mybooks(request):
    user = request.user
    student = user.student
    print(student.books.all())
    books = student.books.all()
    return render(request, "books/student_books.html", {"books":books})

def returnBook(request, bookID):
    book = Book.objects.get(pk = bookID)
    user = request.user
    student = user.student
    book.status = 't'
    student.books.remove(book)
    book.return_date = None
    book.save()
    return redirect('studentBooks')

staff_member_required(login_url=('login'))
def borrowed_books(request):
    books = Book.objects.filter(status='f')
    return render(request, "books/borrowed_books.html", {"books":books})    



staff_member_required(login_url='login')
def editBook(request, bookID):
    book = Book.objects.get(pk=bookID)
    prev_book = {"name":book.name, "price":book.price, "description":book.description, "img":book.img, "category":book.category}
    form = BookModelForm(request.POST or None, initial=prev_book)
    if form.is_valid():
        book.name = form.cleaned_data.get('name')
        book.price = form.cleaned_data.get('price')
        book.description = form.cleaned_data.get('description')
        book.img = form.cleaned_data.get('img')
        book.category = form.cleaned_data.get('category')
        book.save()
        messages.success(request, f"Book {book.name} Edited Successfuly!")

    return render(request, "books/editbook.html", {"book": book, "editform":form})


staff_member_required(login_url='login')
def addBook(request):
    form = BookModelForm(request.POST or None)
    if form.is_valid():
        book_name = form.cleaned_data['name']
        form.save()
        messages.success(request, f"Book {book_name} Added Successfuly!")
        return redirect('home')
    return render(request, "books/addbook.html", {"editform":form})


staff_member_required(login_url='login')
def delBook(request, bookID):
    book = get_object_or_404(Book, pk=bookID)
    if book:
        book.delete()
    return redirect('home')


def searchBook(request):
    bookname = request.POST['search_word']
    results = Book.objects.filter(name__icontains=bookname)
    return render(request, "books/searchbooks.html", {"books":results})



