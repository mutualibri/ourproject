from django.urls import path
from quote.views import create_product_flutter, quotes_page, add_quote, edit_quote, delete_quote, show_json, show_json_by_id, add_quote_ajax\
, get_quote

app_name = 'quote'

urlpatterns = [
    path('', quotes_page, name='quotes_page'),
    path('add-quote', add_quote, name='add_quote'),
    path('edit-quote/<int:id>/', edit_quote, name='edit_quote'),
    path('delete-quote/<int:id>/', delete_quote, name='delete_quote'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('get-quote/', get_quote, name='get_quote'),
    path('add-quote-ajax/', add_quote_ajax, name='add_quote_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]