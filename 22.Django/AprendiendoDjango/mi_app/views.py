from django.shortcuts import render, HttpResponse, redirect

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
