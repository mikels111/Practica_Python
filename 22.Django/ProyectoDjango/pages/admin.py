from django.contrib import admin
from .models import Page

# Configuración extra


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content') # Esto es para que en la pagina de admin de paginas aparezca un buscador
    list_filter = ('visible',) # Esto es para que nos aparezca un seleccionador de filtros para las paginas; este filtro es para seleccionar entre las páginas que estén visibles y las que no
    list_display = ('title','visible','slug','created_at') # Esto es para que aparezcan columnas de los campos de las páginas
    ordering = ('created_at',) # Para el orden en que serán mostradas la páginas; si se le pone un '-' por delante se invierte el orden

# Register your models here.
admin.site.register(Page, PageAdmin)

# Titulos de la pagina de gestión
title = 'Proyecto con Django'
subtitle = 'Panel de gestión'

admin.site.site_header = title
admin.site.site_title = title  # título segundo en la pestaña del navegador
# título primero en la pestaña del navegador y titulo en el body
admin.site.index_title = subtitle
