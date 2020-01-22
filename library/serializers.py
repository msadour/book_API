"""
Classes Serializers.
"""

from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Class who serialize a book instance.
    """
    class Meta:
        model = Book
        fields = ['owner', 'title', 'description', 'isbn', 'date_published']