from django.db import models

# Create your models here.
class Book(models.Model):
    number = models.IntegerField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    voters = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    page_count = models.IntegerField(null=True, blank=True)
    generes = models.TextField(null=True, blank=True)
    ISBN = models.IntegerField(null=True, blank=True)
    language = models.TextField(null=True, blank=True)
    published_date = models.TextField(null=True, blank=True)