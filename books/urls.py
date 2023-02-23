from django.urls import path
from books.views import books, viewBook, borrowBook, mybooks, returnBook, borrowed_books, editBook, addBook, delBook, searchBook

urlpatterns = [
    path('', books, name='home'),
    path('book/<int:bookID>', viewBook, name='viewBook'),
    path('book/<int:bookID>/borrow', borrowBook, name='borrowBook'),
    path('studentbooks', mybooks, name='studentBooks'),
    path('return/<int:bookID>',returnBook, name='returnBook' ),
    path('borrowed_books', borrowed_books, name='borrowed_books'),
    path('editbook/<int:bookID>', editBook, name='editBook'),
    path('delbook/<int:bookID>', delBook, name='delBook'),
    path('addbook', addBook, name='addBook'),
    path('searchbook', searchBook, name='searchBook' )
]