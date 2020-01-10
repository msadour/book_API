from django.core.management.base import BaseCommand
from library.factories import BookFactory, UserFactory


class Command(BaseCommand):
    help = 'Create books'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        owner = UserFactory.build()
        owner.save()

        for _ in range(0, options['number']):
            new_book = BookFactory(
                owner=owner,
            )
            new_book.save()

        self.stdout.write(str(options['number']) + " books was created.")
