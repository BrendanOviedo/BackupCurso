animales = ['perro', 'gato', 'perico', 'alacran']
for animal in animales:
    print(f"ahora la variable animal es {animal}")    
#recorriendo la lista numeros y multiplicando por 2 
numeros = [11,22,33,44,55]
for numero in numeros:
    numero = numero * 2
    print(numero)
#iterar multiples listas 
for numero,animal in zip(numeros, animales):
    print(f"Recorriendo Lista 1 {animal}")
    print(f"Recorriendo Lista 2 {numero}")
#Forma incorrecta de navegar una lista (No funciona en conjuntos set)
    for num in range(len(numeros)):
        print(numeros[num])
#Forma correcta de recorrer una lista por indice usando el for/else
for num in enumerate(numeros):
    Indice = (num[0])
    Valor = (num[1])
    print(f"El indice es {Indice} y el valor es {Valor} ")
else:
    print("Se ejecuto la lista completa")       

        
        


