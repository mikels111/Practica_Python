from django.shortcuts import render, HttpResponse

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
</ul>
<hr/>
"""

def index(request):
    html = """
        <h1>Inicio</h1>    
        <ul>
    """
    year = 2020
    while year <=2080:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year +=1

    html += "</ul>"
    return HttpResponse(layout+html)

def hola_mundo(request):
    return HttpResponse(layout+"""
        <h1>Hola mundo</h1>
        <h2>Esto es Django</h2>
    """)
def pagina(request):
    return HttpResponse(layout+"""
        <h1>Esto es la primera página</h1>
        <h2>Creado por Mikel Seara</h2>
    """)

def contacto(request, nombre, apellido):
    return HttpResponse(layout+f"<h1>Contacto {nombre} {apellido}</h1>")

