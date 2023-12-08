from django.urls import path
from lend.views import create_lend_flutter, show_catalog, get_catalog_json, get_book, get_book_json, preview_lend, show_json, show_sorted, get_book_new, delete_lend_flutter

app_name = 'lend'

urlpatterns = [
    path('', show_catalog, name='show_catalog'),
    path('get-catalog/', get_catalog_json, name='get_catalog_json'),
    path('get-one-book/<int:id>/', get_book, name='get_book'),
    path('get-book-json/<int:id>/', get_book_json, name="get_book_json"),
    path('get-one-book/<int:id>/preview-lend/', preview_lend, name="preview_lend"),
    path('json/', show_json, name='show_json'),
    path('filter/', show_sorted, name='filter'),
    path('get-book-new/<int:id>/', get_book_new, name='get_book_new'),
    path('create-lend-flutter/', create_lend_flutter, name="create_lend_flutter"),
    path('delete-lend-flutter/', delete_lend_flutter, name="delete_lend_flutter"),
]