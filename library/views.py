# -*- coding: utf-8 -*-
"""
Views.
"""


from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrReadOnly
from .models import Book
from .serializers import BookSerializer


class HelloView(APIView):
    """
    Display the message 'Hello World!' if the permission allows us.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class BookViewSet(viewsets.ModelViewSet):
    """
    Display book(s) if the permission allows us.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated,
        permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

