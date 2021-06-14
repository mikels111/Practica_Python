from django.contrib import admin
from .models import Page


# Register your models here.
admin.site.register(Page)

# Titulos de la pagina de gestión
title = 'Proyecto con Django'
subtitle = 'Panel de gestión'

admin.site.site_header = title
admin.site.site_title = title #título segundo en la pestaña del navegador
admin.site.index_title = subtitle #título primero en la pestaña del navegador y titulo en el body
