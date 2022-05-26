from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from books.models import Book
import datetime


def index_view(request):
    return redirect('books')


def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': books
    }
    return render(request, template, context=context)


def books_date_view(request, date: datetime):
    page_number_request = request.GET.get('page', 1)
    paginator = Paginator(Book.objects.all().order_by('pub_date'), 1)
    page = paginator.get_page(page_number_request)
    try:
        next_page = paginator.get_page(page.next_page_number()).object_list[0].pub_date
    except:
        next_page = None
    try:
        previous_page = paginator.get_page(page.previous_page_number).object_list[0].pub_date
    except:
        previous_page = None
    template = 'books/books_list.html'
    context = {
        'books': page.object_list,
        'page': page,
        'next_page': next_page,
        'previous_page': previous_page,
    }
    return render(request, template, context)
