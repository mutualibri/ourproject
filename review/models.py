from django.db import models
from django.contrib.auth.models import User
from book.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime

class Item(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=True)
    review = models.TextField(max_length=1000, null=True)
    rating = models.IntegerField(default=0, 
                                validators=[
                                MinValueValidator(0, message='Minimum rating is 0!'),
                                MaxValueValidator(100, message='Maximum rating is 100!')
    ], null=True)
    date_added = models.DateField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date_added']


class Review(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, null=True)
    likes_count = models.IntegerField(default=False)
    dislikes_count = models.IntegerField(default=False)


@receiver(pre_save, sender=Review)
def update_review_counts(sender, instance, **kwargs):
    likes = instance.reviews.filter(liked=True).count()
    dislikes = instance.reviews.filter(liked=False).count()

    instance.likes_count = likes
    instance.dislikes_count = dislikes
