from django.core.management.base import BaseCommand
import json
from books.models import Book


class Command(BaseCommand):
    help = 'Import books to database'

    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r') as file:
            books = json.load(file)
            for book in books:
                Book(
                    name=book['fields']['name'],
                    author=book['fields']['author'],
                    pub_date=book['fields']['pub_date']
                ).save()

    def add_arguments(self, parser):
        pass