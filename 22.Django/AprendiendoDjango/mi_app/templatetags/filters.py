from django import template

register = template.Library()


@register.filter(name='saludo')
def saludo(value):
    if len(value) >= 8:
        largo = '<p>Tu nombre es muy largo</p>'
    return f"<h1 style='color:red; background:lightblue'>Bienvenido {value}</h1>"
