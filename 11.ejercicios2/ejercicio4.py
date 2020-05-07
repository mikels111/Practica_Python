"""def getTipo(var):
    if type(var) == list:
        print(f"la variable {var} es de tipo lista")
    elif type(var) == str:
        print(f"la variable {var} es de tipo String")
    elif type(var) == int:
        print(f"la variable {var} es de tipo entero")
    elif type(var) == bool:
        print(f"la variable {var} es de tipo boolean")"""

def comprobar(var, tipo):
    comprobacion = isinstance(var, tipo)
    tipo_de_dato = ""

    if comprobacion:
        tipo_de_dato = f"El tipo de dato es {tipo}"

    return tipo_de_dato

lista = [4, 9, 43, 3]
texto = "hola"
entero = 89
buleano = True

print(comprobar(lista, list))

"""getTipo(lista)
getTipo(texto)
getTipo(entero)
getTipo(buleano)"""
