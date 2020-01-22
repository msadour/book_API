"""
Command for create and loaded profile(s).
"""

from django.core.management.base import BaseCommand
from factory.faker import faker

from library.factories import UserFactory, ProfilFactory


class Command(BaseCommand):
    """
    Class command.
    """

    help = 'Create books'

    def add_arguments(self, parser):
        """
        Add, as argument, the number of profile to created.
        :param parser: The parser
        """

        parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        """
        Execute the command that create profile(s).
        """

        for _ in range(0, options['number']):
            new_faker = faker.Faker()

            user = UserFactory(
                username=new_faker.email(),
                email=new_faker.email(),
                password='qwertz'
            )

            ProfilFactory(
                user=user,
            )
