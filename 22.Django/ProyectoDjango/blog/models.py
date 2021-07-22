from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=255, verbose_name='Descripcion')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    # Clave foránea de 'Usuarios'(user)
    user = models.ForeignKey(
        User,editable=False, verbose_name='Usuario', on_delete=models.CASCADE)# El parametro editable es para que el campo no se pueda editar
    categories = models.ManyToManyField(
        Category, verbose_name='Categorías', blank=True)  # Relacion de varios a varios
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen',upload_to="articles")
    public = models.BooleanField(verbose_name='Público')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Editado el')


    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
