from django.test import TestCase
from django.urls import reverse
from .models import Book
# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Think and grow rich",
            subtitle = "Be rich",
            author = "John",
            isbn = 1234567891234

        )
    def test_book_content(self):
        self.assertEqual(self.book.title,"Think and grow rich")
        self.assertEqual(self.book.subtitle,"Be rich")
        self.assertEqual(self.book.author,"John")
        self.assertEqual(self.book.isbn,1234567891234)

    def test_book_listview(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Be rich")
        self.assertTemplateUsed(response,"books/book_list.html")