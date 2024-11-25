
from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer
# Create your views here.

class BookApiView(generics.ListAPIView):
    #specifying the queryset and serializer
    queryset = Book.objects.all()
    serializer_class = BookSerializer
