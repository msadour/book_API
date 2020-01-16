# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
#
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal


from .singleton import SingletonModel
from celery import shared_task


class Profile(models.Model):
    """
    Class Profile
    """
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photo/', default='profile_photo/photo.jpeg')

    def get_username(self):
        return self.user.username


@receiver(post_save, sender=Profile)
def new_user(sender, **kwargs):
    new_profile = kwargs.get('instance')
    print("The user " + new_profile.get_username() + " has been created.")


def init_profil():

    user = User.objects.get(username='test')
    profile = Profile(user=user)
    print(profile.profile_photo.name)
    print(profile.profile_photo.path)


class Settings(SingletonModel):
    """
    Class Settings
    """
    theme = models.CharField(max_length=300, default='dark')
#
#
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

