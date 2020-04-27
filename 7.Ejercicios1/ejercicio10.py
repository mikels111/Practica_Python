# Pedir la nota de 9 alumnos y que diga cuantos han aprobado y cuantos suspendidos
contador_aprobados = 0
contador_supendidos = 0

for cont in range(1, 10):
    nota = int(input(f"Escribe la nota del alumno {cont}: "))
    if nota >= 5 and nota < 11:
        contador_aprobados += 1
    elif nota < 5 and nota > 0:
        contador_supendidos += 1
    else:
        print("Nota no admitida")

print(f"Aprobados {contador_aprobados}")
print(f"Suspendidos {contador_supendidos}")