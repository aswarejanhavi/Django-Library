from django.shortcuts import render


# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Book, Borrower
from .serializers import BookSerializer, BorrowerSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer

class BorrowerListCreate(generics.ListCreateAPIView):
    queryset = Borrower.objects.all()
    serializer = BorrowerSerializer

class BorrowerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrower.objects.all()
    serializer = BorrowerSerializer

class BorrowBook(generics.GenericAPIView):
    serializer_class = BookSerializer

    def post(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            if not book.available:
                return Response({'error': 'Book is already borrowed'}, status=status.HTTP_400_BAD_REQUEST)
            book.available = False
            book.save()
            return Response(BookSerializer(book).data)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ReturnBook(generics.GenericAPIView):
    serializer_class = BookSerializer

    def post(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            if book.available:
                return Response({'error': 'Book is not borrowed'}, status=status.HTTP_400_BAD_REQUEST)
            book.available = True
            book.save()
            return Response(BookSerializer(book).data)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
