"""
Class Singleton
"""
from django.db import models


class SingletonModel(models.Model):
    """
    Class Singleton.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Make sure that we can save only one object.
        """
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        """
        Get or create an objects.
        """
        obj, created = cls.objects.get_or_create(pk=1)
        return obj