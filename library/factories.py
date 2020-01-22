"""
Factories classes.
"""

import factory
from factory.faker import faker

from .models import User, Book, Profile

FAKE = faker.Faker()


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

    username = FAKE.email()
    email = FAKE.email()
    password = 'qwertz'

    class Meta:
        model = User


class ProfilFactory(factory.django.DjangoModelFactory):
    """
    Class ProfileFactory.
    """

    class Meta:
        model = Profile

