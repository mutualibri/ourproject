from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from lend.models import Lend
from book.models import Book
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from datetime import date, timedelta
from .models import User
from lend.forms import LendForm, BookFilterForm
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='book/login')
def show_catalog(request):  
    books = Book.objects.all()
    context = {
        'books':books,
        'name':request.user.username,
        'images':['https://www.booktopia.com.au/covers/big/9781612626796/0000/attack-on-titan-vol-13.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0N5d_ivUHjwRT-biqpXzfCESXuS4VmTc9xcnghMRtUr7c4mbck4AjPDRdhDHGouwHcjI&usqp=CAU', ],
    }

    return render(request, "catalog.html", context)

def show_sorted(request): 
    form = BookFilterForm(request.GET)  # Gunakan request.GET untuk mendapatkan parameter filter dari URL
    books = Book.objects.all()

    if form.is_valid():
        title = form.cleaned_data.get('title')
        author = form.cleaned_data.get('author')

        if title:
            books = books.filter(title__icontains=title)

        if author:
            books = books.filter(author__icontains=author)

    context = {
        'books': books,
        'name': request.user.username,
        'images': ['https://www.booktopia.com.au/covers/big/9781612626796/0000/attack-on-titan-vol-13.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0N5d_ivUHjwRT-biqpXzfCESXuS4VmTc9xcnghMRtUr7c4mbck4AjPDRdhDHGouwHcjI&usqp=CAU', ],
        'form': form,  # Tambahkan form ke dalam konteks
    }

    return render(request, "filter.html", context)

def get_catalog_json(request):
    product_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def get_book_new(request, id):
    url = reverse('get_book', args=[id])
    return HttpResponseRedirect(url)

def get_book(request, id):
    books = Book.objects.filter(pk=id)
    user= request.user
    context = {
        'books':books,
        'id':id,
        'user':user,
    }
    return render(request, "book_view.html", context)

def get_book_json(request, id):
    product_item = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', product_item))

def preview_lend(request, id):
    book = Book.objects.get(pk=id)
    form = LendForm(request.user, book.id)
    
    if request.method == 'POST':
        form = LendForm(request.user, book.id, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lend:show_catalog'))
            # Redirect atau lakukan apa yang diperlukan setelah pengajuan pinjaman
    return render(request, 'preview_lend.html', {'form': form, 'book': book, 'id':id})
    
def show_json(request):
    data = Lend.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")