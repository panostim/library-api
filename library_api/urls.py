from django.urls import path

from books.views import list_books

urlpatterns = [
    path('list', list_books, name='list-books'),
]
