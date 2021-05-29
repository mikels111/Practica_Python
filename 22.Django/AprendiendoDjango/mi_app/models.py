from django.db import models

# Create your models here.


class Article(models.Model):
    # El vervose_name es para decir como se va ver en el panel de control de Django
    title = models.CharField(max_length=100, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to='articles')
    public = models.BooleanField(verbose_name='Publicado')# auto_now_add en true indica cuando se crea
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')# auto_now indica cuando se actualiza
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:  # Para mostrar como queramos en el panel de control
        verbose_name = 'Articulo'  # Para decirle como se va llamar el modelo en singular
        verbose_name_plural = 'Articulos'
        ordering = ['-create_at']  # sin el guión es ascendente

    def __str__(self):  # Para mostrar los campos que quieras como nombre del modelo
        if self.public:
            publico = "(Publicado)"

        else:
            publico = '(Privado)'

        return f"{self.title} {publico}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


# Para cambiar un campo en las tablas en Models.py y que se refleje en sqlite:
# - Hacer un cambio en models.py
# - En la carpeta donde está manage.py: python mange.py makemigrations
# - python manage.py sqlmigrate mi_app 0002<--numero del migrate que está en la carpeta migrations
# -python manage.py migrate
