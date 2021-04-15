from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='null')
    public = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)#auto_now_add en true indica cuando se crea
    updated_at = models.DateTimeField(auto_now=True)#auto_now indica cuando se actualiza


class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    created_at=models.DateField()

# Para cambiar un campo en las tablas en Models.py y que se refleje en sqlite:
# - Hacer un cambio en models.py
# - En la carpeta donde está manage.py: python mange.py makemigrations
# - python manage.py sqlmigrate mi_app 0002<--numero del migrate que está en la carpeta migrations
# -python manage.py migrate