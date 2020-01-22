# -*- coding: utf-8 -*-
"""
Tests.
"""
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .factories import UserFactory, BookFactory
from .models import Settings


class BookTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_test = UserFactory()
        self.client.force_authenticate(user=self.user_test)
        self.book = BookFactory(
            owner=self.user_test,
        )

    def test_list(self):
        # Request our API to get books.
        # Check if we get the request code as 200.

        response = self.client.get('/books/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve(self):
        # Request our API to get a specific book.
        # Check if we get the request code as 200.

        response = self.client.get(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        # Ceate a new book
        # Send it to our API
        # Checked if it worked (by the code 200)

        data_book = {'owner': self.user_test.id,
                    'title': 'test title',
                    'description': 'test description',
                    'isbn': 'test isbn'
                    }
        response = self.client.post('/books/', data=data_book)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        # Delete a specific book
        # get the list of all books
        # Check if the list is empty

        self.client.delete('/books/' + str(self.book.id) + '/')

        request = self.client.get('/books/').data
        self.assertEqual(len(request), 0)

    def test_partial_update(self):
        # Create a book
        # request our API to update his title with 'new title'
        # Check if the title has been updated

        book = BookFactory.create(
            owner=self.user_test,
        )
        book.save()

        request = self.client.patch('/books/' + str(book.id) + '/', data={'title': 'new title'})
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_update(self):
        # Create a book
        # Create a new objects (book_updated)
        # request our API to update the created book by using book_updated
        # Check if the book has been updated

        book = BookFactory.create(
            owner=self.user_test,
        )
        book.save()
        book_updated = {'owner': self.user_test.id,
                         'title': 'new test title',
                         'description': 'test description',
                         'isbn': 'test isbn'
        }
        request = self.client.put('/books/' + str(book.id) + '/', data=book_updated)

        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_singleton(self):
        # Create an object setting
        # Load another setting object
        # Check if the two objects are equal

        settings = Settings(theme='theme')
        settings.save()
        another_settings = Settings.load()
        assert settings == another_settings
