from django.urls import path
from review.views import create_review_flutter, show_main, create_review_ajax, create_review, show_json,show_json_by_id
from . import views

app_name = 'review'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add_review', create_review, name='create_review'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('show-main/recent/', views.show_main, {'sort_order': 'recent'}, name='show_main_recent'),  
    path('show-main/oldest/', views.show_main, {'sort_order': 'oldest'}, name='show_main_oldest'),  
    path('create-flutter/', create_review_flutter, name='create_review_flutter'),
]