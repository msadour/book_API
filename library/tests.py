# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
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
        response = self.client.get('/books/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve(self):
        response = self.client.get(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        data_book = {'owner': self.user_test.id,
                    'title': 'test title',
                    'description': 'test description',
                    'isbn': 'test isbn'
                    }
        response = self.client.post('/books/', data=data_book)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        self.client.delete('/books/' + str(self.book.id) + '/')

        request = self.client.get('/books/').data
        self.assertEqual(len(request), 0)

    def test_partial_update(self):
        book = BookFactory.create(
            owner=self.user_test,
        )
        book.save()

        request = self.client.patch('/books/' + str(book.id) + '/', data={'title': 'new title'})
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_update(self):
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
        settings = Settings(theme='theme')
        settings.save()
        another_settings = Settings.load()
        assert settings == another_settings
