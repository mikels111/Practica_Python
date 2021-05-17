from django.shortcuts import render, HttpResponse, redirect
from mi_app.models import Article
from django.db.models import Q  # Para hacer consultas con 'or'
from mi_app.forms import FormArticle
from django.contrib import messages
# Create your views here.
# MVC = modelo vista controlador --> acciones (métodos)
#        ||      ||       ||
# MVT = modelo template vista --> acciones (métodos)


layout = """
<h1>Sitio web con Django</h1>
<hr/>
<ul>
    <li><a href="/inicio">Inicio</a></li>
    <li><a href="/hola_mundo">Hola mundo</a></li>
    <li><a href="/pagina">Pagina pruebas</a></li>
    <li><a href="/contacto">Contacto</a></li>
</ul>
<hr/>
"""


def index(request):
    # html = """
    #     <h1>Inicio</h1>
    #     <ul>
    # """
    # year = 2020
    # while year <= 2080:
    #     if year % 2 == 0:
    #         html += f"<li>{str(year)}</li>"
    #     year += 1

    # html += "</ul>"

    year = 2021
    hasta = range(year, 2051)

    nombre = 'Mikel'
    lenguajes = ['Javascript', 'Python', 'Java']

    return render(request, 'index.html', {
        'mi_variable': 'soy un dato que está en la vista',
        'title': 'Inicio desde views',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })
    # return HttpResponse(layout + html)


def hola_mundo(request):
    return render(request, 'hola_mundo.html')


def pagina(request, redirigir=0):
    if redirigir == 1:
        # return redirect("inicio")# inicio es el nombre de la url
        # el nombre "contacto" es el atributo "name" de la url no la ruta
        return redirect("contacto", nombre="Antonio", apellido="seara")
    return render(request, 'pagina.html', {
        'texto': 'Esto es un texto',
        'lista': ['uno', 'dos', 'tres']
    })


def contacto(request, nombre="", apellido=""):
    html = ""
    if nombre and apellido:
        html += "<p>El nombre es :</p>"
        html += f"<h2>{nombre} {apellido}</h2>"
    return HttpResponse(layout+f"<h1>Contacto</h1>"+html)


def crear_articulo(request, title, content, public):
    articulo = Article(
        title=title,
        content=content,
        public=public
    )

    articulo.save()

    return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> {articulo.content}")


def save_article(request):

    if request.method == 'POST':
        title = request.POST['title']

        if len(title) <= 5:
            return HttpResponse('El título es muy pequeño')

        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title=title,
            content=content,
            public=public
        )

        articulo.save()

        return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> {articulo.content}")
    else:
        return HttpResponse(f"No se ha podido crear el articulo")


def create_article(request):

    return render(request, 'create_article.html')


def create_full_article(request):
    if request.method == 'POST':

        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            # para coger lo que llegue con get con la variable title
            title = data_form.get('title')
            # para coger de lo que llegue con la variable content
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title=title,
                content=content,
                public=public
            )

            articulo.save()
            # crear mensaje flash(sesión que sólo se muestra una vez)
            messages.success(request, f'Articulo creado correctamente {articulo.id}')#mensajes que solo se muestra una vez

            return redirect('articulos') # nombre de la url a la que quieres que te lleve

            # return HttpResponse(title+'----'+content+'----'+str(public))
    else:
        formulario = FormArticle()

    return render(request, 'create_full_article.html', {
        'form': formulario
    })


def articulo(request):
    try:
        # El metodo 'get' saca un objeto(registro) del modelo
        articulo = Article.objects.get(title="tercer articulo", public=True)
        response = f"articulo:{articulo.id}->{articulo.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)


def editar_articulo(request, id):

    articulo = Article.objects.get(pk=id)
    articulo.title = "El caballero oscuro"
    articulo.content = "Pelicula del 2008"
    articulo.public = True
    articulo.save()

    response = f"articulo:{articulo.id}->{articulo.title} {articulo.content}"
    return HttpResponse(response)


def articulos(request):
    # [:3], en vez de all si ponemos order_by() se ordena por id, también se puede poner order_by(title) por la columna title
    articulos = Article.objects.all()
    # [:3] es el limit, también se puede poner [3:7] para mostrar solo del 3 al 7 sin incluir el 3

    # se pueden poner mas de una condicion
    # articulos = Article.objects.filter(id__gte=6)
    # gt es greater than, gte para mayores e igual al numero,lt es less than: menores a el numero, lte menores o igual al numero

    # articulos = Article.objects.filter(
    #     title__contains='articulo')  # Condicion que contenga articulo, también se puede poner title__exact y title__iexact
    # articulos = Article.objects.filter(title='articulo', id=3)# Condicion

    # articulos = Article.objects.filter(title='articulo').exclude(public=True)#exclude va a excluir a los que tengan el campo public a true
    # articulos = Article.objects.raw('SELECT * FROM mi_app_article')

    # articulos = Article.objects.filter(Q(content__contains='nuevo')| Q(content__contains='3'))#la Q es necesaria para hacer consultas con 'or'
    return render(request, 'articulos.html', {
        'articulos': articulos
    })


def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')
