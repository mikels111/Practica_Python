"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# importar app con mis vistas
# from mi_app import views
import mi_app.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola_mundo/', mi_app.views.hola_mundo, name='hola_mundo'),
    path('inicio/', mi_app.views.index, name='inicio'),
    path('pagina/', mi_app.views.pagina, name='pagina'),
    path('pagina/<int:redirigir>', mi_app.views.pagina, name='pagina'),
    path('',mi_app.views.index, name='index'),
    path('contacto/',mi_app.views.contacto, name='contacto'),
    path('contacto/<str:nombre>/',mi_app.views.contacto, name='contacto'),
    path('contacto/<str:apellido>',mi_app.views.contacto, name='contacto'),
    path('contacto/<str:nombre>/<str:apellido>',mi_app.views.contacto, name='contacto'),
    path('crear_articulo/<str:title>/<str:content>/<str:public>', mi_app.views.crear_articulo, name='crear_articulo'),
    path('articulo/', mi_app.views.articulo, name='articulo'),
    path('articulo_edit/<int:id>', mi_app.views.editar_articulo, name='editar_articulo'),
    path('articulos/', mi_app.views.articulos, name='articulos')
]
