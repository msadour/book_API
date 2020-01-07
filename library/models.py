# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from .singleton import SingletonModel
from celery import shared_task


class Settings(SingletonModel):
    theme = models.CharField(max_length=300, default='dark')


class PublishManager(models.Manager):
    def republish(self, new_date):
        self.get_queryset().all().update(date_published=new_date)


class Notification(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)


class Book(models.Model):
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    isbn = models.CharField(max_length=100)
    date_published = models.DateTimeField(default=datetime.now)
    objects = PublishManager()

    @shared_task
    def send_notification(self, number=10):
        self.create_notification.delay(number)
        messages.success("We sent " + str(number) + " notifications.")

    def create_notification(self, number=10):
        receiver = User.objects.get(username='test')
        for num_book in range(number):
            Notification(
                sender=self.owner,
                receiver=receiver,
                text= str(num_book) + " book (" + self.title + ") are available"

            ).save()

