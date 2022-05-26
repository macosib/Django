from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import books to database'

    def handle(self, *args, **options):
        pass
        # with open('phones.csv', 'r') as file:
        #     phones = list(csv.DictReader(file, delimiter=';'))

    def add_arguments(self, parser):
        pass