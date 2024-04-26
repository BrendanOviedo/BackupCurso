
#Creando listas
cadena = "Hola mundo"
frutas = ['manzana', 'pera', 'pejibaye', 'banano', 'fresa', 'melocoton']
numeros = [22, 10, 11, 55, 40]
#continuar bucle saltando la cadena dada

for fruta in frutas:
    if fruta == 'pera':
        continue
    print(f"me comi una {fruta}")
 
#terminar bucle no ejecuta nada mas despues del break

for fruta in frutas:
    if fruta == 'pera':
        break
    print(f"me comi una {fruta}")
else:
    print("bucle terminado")
    
#iterar cadena de texto

for letra in cadena:
    print(letra)
    
#Duplicar numeros en una sola linea
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)



