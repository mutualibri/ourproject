from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)
    quotes = models.TextField(max_length=255)
