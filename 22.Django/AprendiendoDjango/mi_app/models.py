from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    public = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)#auto_now_add en true indica cuando se crea
    updated_at = models.DateTimeField(auto_now=True)#auto_now indica cuando se actualiza


class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    created_at=models.DateField()
