from django.urls import path
from books.views import books_view, index_view, books_date_view
from django.urls import register_converter
from . import converters

register_converter(converters.DateConverter, 'date')

urlpatterns = [
    path('', index_view),
    path('books/', books_view, name='books'),
    path('books/<date:date>/', books_date_view, name='book_date'),
]
