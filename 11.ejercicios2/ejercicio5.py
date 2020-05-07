juegos = [
    {
        "genero" : "Acción",
        "juego1" : "gta",
        "juego2" : "cod",
        "juego3" : "pugb"
    },
    {
        "genero" : "aventura",
        "juego1" : "assasins",
        "juego2" : "crash",
        "juego3" : "Prince Of Persia"
    },
    {
        "genero" : "deportes",
        "juego1" : "fifa",
        "juego2" : "pes",
        "juego3" : "Moto gp"
    }
]
# tipo 1
for genero in range(0, 3):
    print(juegos[genero]["genero"]) 
    print("---------------")
    print(juegos[genero]["juego1"])   
    print(juegos[genero]["juego2"])
    print(juegos[genero]["juego3"])
    print("---------------")
# tipo 2
for genero in juegos:
    print(genero["genero"])
    print("---------------")
    print(genero["juego1"])
    print(genero["juego2"])
    print(genero["juego3"])
    print("---------------")
    