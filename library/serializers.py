from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['owner', 'title', 'description', 'isbn', 'date_published']