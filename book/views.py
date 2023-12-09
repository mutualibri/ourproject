from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from django.core import serializers
from book. models import Book
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }

    return render(request, "index.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('book:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lend:show_catalog')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('book:login')

def get_books_by_json (request):
    data = Book.objects.all ()
    return HttpResponse (serializers.serialize("json", data), content_type="application/json")

def get_books_by_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        books = Book.objects.filter(title__contains=searched)
        return render(request, 'search.html', {'searched': searched, 'books': books})
    else:
        return render(request, 'search.html', {})

def get_product_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
