import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from quote.forms import QuoteForm
from django.urls import reverse
from quote.models import Quotes
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def quotes_page(request):
    sort_order = request.GET.get('sort_order', 'recent')  # Defaultnya, urutkan berdasarkan yang terbaru

    if sort_order == 'recent':
        quotes = Quotes.objects.all().order_by('-id')  # Urutkan berdasarkan yang terbaru (default)
    else:
        quotes = Quotes.objects.all().order_by('id')  # Urutkan berdasarkan yang terlama

    context = {
        'name': "nama",
        'quotes': quotes,
        'sort_order': sort_order,
    }

    return render(request, "quotes.html", context)

def add_quote(request):
    form = QuoteForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        quote = form.save(commit=False)
        quote.user = request.user
        quote.username = request.user.username
        quote.save()
        return HttpResponseRedirect(reverse('quote:quotes_page'))

    context = {'form': form}
    return render(request, "add_quote.html", context)


def edit_quote(request, id):
    quote = Quotes.objects.get(pk = id)
    form = QuoteForm(request.POST or None, instance=quote)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('quote:quotes_page'))
    
    context = {'form': form}
    return render(request, "edit_quote.html", context)
    
def delete_quote(request, id):
    quote = Quotes.objects.filter(pk=id)
    quote.delete()

    return redirect('quote:quotes_page')

def show_json(request):
    data = Quotes.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Quotes.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_quote(request):
    quotes = Quotes.objects.all()
    return HttpResponse(serializers.serialize('json', quotes))

@csrf_exempt
def add_quote_ajax(request):
    if request.method == 'POST':
        book_name = request.POST.get("book_name")
        quotes = request.POST.get("quotes")
        user = "request.user"

        new_quote = Quotes(book_name=book_name, quote=quotes, user=user, username = user.username)
        new_quote.save()    

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Quotes.objects.create(
            user = request.user,
            book_name = data["book_name"],
            quotes = data["quotes"],
            username = request.user.username,
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)