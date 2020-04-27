# Mostrar todas la tablas de multiplicar 

for contador in range(1 ,11):
    print("/////////tabla del "+str(contador))
    
    for contador2 in range(1, 11):
        print(f"{contador} x {contador2} = {contador * contador2}")