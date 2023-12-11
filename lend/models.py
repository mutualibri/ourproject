from django.db import models
from django.contrib.auth.models import User
from book.models import Book

# Create your models here.
class Lend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    number = models.IntegerField()
