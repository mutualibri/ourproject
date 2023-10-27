from django.shortcuts import render
from .models import Lend
from book.models import Book
from django.http import HttpResponse
from django.core import serializers
from datetime import date, timedelta

# Create your views here.
def show_catalog(request):
    books = Book.objects.all()
    context = {
        'books':books,
        'images':['https://www.booktopia.com.au/covers/big/9781612626796/0000/attack-on-titan-vol-13.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0N5d_ivUHjwRT-biqpXzfCESXuS4VmTc9xcnghMRtUr7c4mbck4AjPDRdhDHGouwHcjI&usqp=CAU', ],
    }

    return render(request, "catalog.html", context)

def get_catalog_json(request):
    product_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def get_book(request, id):
    books = Book.objects.filter(pk=id)
    context = {
        'books':books,
        'id':id,
    }
    return render(request, "book_view.html", context)

def get_book_json(request, id):
    product_item = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', product_item))

def preview_lend(request, id):
    book = Book.objects.filter(pk=id)
    context = {
        'book':book,
        'id':id,
    }
    return render(request, "preview_lend.html", context)

def create_lend(request, id):
    current_date = date.today()
    future_date = current_date + timedelta(days=7)


    user = request.user
    book = Book.objects.get(pk=id)
    new_product = Lend(user=user, number=id, start_date=current_date, end_date=future_date, book=book)
    new_product.save()
    context = {
        'book':book,
        'id':id,
    }
    return render(request, "success_create.html", context)
