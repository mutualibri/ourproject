import json
from django.http import HttpResponseRedirect
from review.forms import ReviewForm
from django.urls import reverse
from django.shortcuts import render
from review. models import Item, Review
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from book.models import Book
from django.contrib.auth.decorators import login_required

@login_required(login_url='book/login')
def show_main(request):
    sort_order = request.GET.get('sort_order', 'recent')  # Defaultnya, urutkan berdasarkan yang terbaru
    if sort_order == 'recent':
        reviews = Item.objects.all().order_by('-id')  # Urutkan berdasarkan yang terbaru (default)
    else:
        reviews = Item.objects.all().order_by('id')  # Urutkan berdasarkan yang terlama

    context = {
        'reviews': reviews,
        'sort_order': sort_order,
        'name':"name",
    }

    return render(request, "mainReview.html", context)


@csrf_exempt
def create_review_ajax(request):
    if request.method == 'POST':
        rating = request.POST.get("rating")
        title = request.POST.get("title")
        date_added = date.today()
        review = request.POST.get("review")
        user = request.user
        new_item = Item(
            title=title,
            review=review,
            date_added=date_added,
            user=user,
            username=user.username,
        )
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def create_review(request):
    form = ReviewForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        review = form.save(commit=False)
        review.user = request.user
        review.username = request.user.username
        form.save()
        return HttpResponseRedirect(reverse('review:show_main'))

    context = {'form': form}
    return render(request, "addReview.html", context)

def show_json(request):
    reviews= Item.objects.all()
    return HttpResponse(serializers.serialize('json', reviews), content_type="application/json")

def show_json_by_id(request, id):
    reviews= Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', reviews), content_type="application/json")

def get_review(request, id):
    reviews = Item.objects.all()
    context = {
        'reviews':reviews,
        'id':id,
    }
    return render(request, "mainReview.html", context)

@csrf_exempt
def toggle_like_dislike(request):
    if request.method == 'POST':
        review_id = request.POST.get("review_id")
        user = request.user

        try:
            review = Item.objects.get(item_id=review_id, user=user)
        except Item.DoesNotExist:
            # Jika review belum ada, buat review baru
            review = Item(item_id=review_id, user=user)

        action = request.POST.get("action")

        if action == "like":
            review.liked = not review.liked
            review.disliked = False
        elif action == "dislike":
            review.disliked = not review.disliked
            review.liked = False

        review.save()

        return HttpResponse("OK", status=200)

    return HttpResponseNotFound()

@csrf_exempt
def create_review_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_review = Item.objects.create(
            rating = int(data["rating"]),
            title = data["title"],
            date_added = date.today(),
            review = data["review"],
            user = request.user,
            username = request.user.username,
        )

        new_review.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)