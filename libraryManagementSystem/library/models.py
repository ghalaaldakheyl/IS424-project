# library/models.py
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    published_date = models.DateField()
    available = models.BooleanField(default=True)
    reserved_by = models.ManyToManyField(User, related_name="reserved_books", blank=True)
    
    def __str__(self):
        return self.title
