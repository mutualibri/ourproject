from django.urls import path
from book.views import get_books_by_json, get_books_by_xml, register, login_user, logout_user, show_main


app_name = 'book'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('json/', get_books_by_json, name='get_book_by_jsons'),
    path('xml/', get_books_by_xml, name='get_by_xml'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]