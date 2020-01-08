# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from .singleton import SingletonModel
from celery import shared_task


class Settings(SingletonModel):
    """
    Class Settings
    """
    theme = models.CharField(max_length=300, default='dark')


class PublishManager(models.Manager):
    """
    Objects manager worked with dates published
    """
    def republish(self, new_date):
        self.get_queryset().all().update(date_published=new_date)


class Notification(models.Model):
    """
    Class Notification
    """
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)


class Book(models.Model):
    """
    Class Book
    """
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    isbn = models.CharField(max_length=100)
    date_published = models.DateTimeField(default=datetime.now)
    objects = PublishManager()

    def send_notification(self, number):
        """
        Send notification to the users.
        """
        self.create_notification.delay(number, self.id)

    @staticmethod
    @shared_task
    def create_notification(number, id_book):
        """
        Create notifications.
        """
        book = Book.objects.get(id=id_book)
        for num_book in range(number):
            Notification(
                sender=book.owner,
                receiver=User.objects.get(username='test'),
                text=str(num_book) + " book (" + book.title + ") are available"

            ).save()

