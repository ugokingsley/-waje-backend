from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *


class AuthorViewSet(viewsets.ViewSet):
    def list(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        author = Author.objects.get(id=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def update(self, request, pk=None):
        author = Author.objects.get(id=pk)
        serializer = AuthorSerializer(instance=author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)



class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def update(self, request, pk=None):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
