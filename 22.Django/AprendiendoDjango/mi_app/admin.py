from django.contrib import admin
from .models import Article, Category # <-- Importacion

class ArticleAdmin(admin.ModelAdmin): #Para que al editar un articulo nos aparezcan los campos que solo sean de lectura
    readonly_fields = ('create_at','updated_at')

# Register your models here.
admin.site.register(Article, ArticleAdmin) #<--modelo articulo
admin.site.register(Category) #<-- modelo categoria