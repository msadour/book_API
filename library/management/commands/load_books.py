"""
Command for create and loaded book(s).
"""

from django.core.management.base import BaseCommand

from library.factories import BookFactory, UserFactory


class Command(BaseCommand):
    """
    Class command.
    """
    help = 'Create books'

    def add_arguments(self, parser):
        """
        Add, as argument, the number of book to created.
        :param parser: The parser
        """

        parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        """
        Execute the command that create book(s).
        """

        owner = UserFactory.build()
        owner.save()

        for _ in range(0, options['number']):
            new_book = BookFactory(
                owner=owner,
            )
            new_book.save()

        self.stdout.write(str(options['number']) + " books was created.")
