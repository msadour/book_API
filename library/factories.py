"""
Factories classes.
"""

import factory
from .models import User, Book


class BookFactory(factory.django.DjangoModelFactory):
    """
    Class BookFactory.
    """

    title = 'test title'
    description = 'test description'
    isbn = 'test isbn'

    class Meta:
        model = Book


class UserFactory(factory.django.DjangoModelFactory):
    """
    Class UserFactory.
    """

    username = factory.Sequence(lambda n: 'person{0}@example.com'.format(n))
    email = factory.Sequence(lambda n: 'person{0}@example.com'.format(n))
    password = 'qwertz'

    class Meta:
        model = User
