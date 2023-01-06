from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    description = models.TextField(null=True, blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 


