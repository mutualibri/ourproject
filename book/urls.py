from django.urls import path
from book.views import get_books_by_json, get_books_by_xml
from . import views

app_name = 'book'

urlpatterns = [
    path('json', get_books_by_json, name='get_book_by_jsons'),
    path('xml', get_books_by_xml, name='get_by_xml'),
]