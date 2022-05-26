import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):

    help = 'Fill in the database Phone'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        print(phones)
        for phone in phones:
            # TODO: Добавьте сохранение модели
            pass
