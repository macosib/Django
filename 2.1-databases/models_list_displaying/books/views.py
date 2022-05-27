from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from books.models import Book
import datetime


def index_view(request):
    return redirect('books')


def books_view(request):
    books = Book.objects.all().order_by('pub_date')
    template = 'books/books_list.html'
    context = {
        'books': books
    }
    return render(request, template, context=context)


def books_date_view(request, date: datetime):
    books = Book.objects.all().filter(pub_date=date)
    try:
        next_book_date = Book.objects.all().filter(pub_date__gt=date).order_by('pub_date')[0].pub_date
    except IndexError:
        next_book_date = None
    try:
        previous_book_date = Book.objects.all().filter(pub_date__lt=date).order_by('pub_date')[0].pub_date
    except IndexError:
        previous_book_date = None
    template = 'books/books_list.html'

    context = {
        'books': books,
        'next_page': next_book_date,
        'previous_page': previous_book_date,
    }
    return render(request, template, context)
