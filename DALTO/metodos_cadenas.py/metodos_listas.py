#creando una lista con list([])

tupla1 = ("Brendan", "Nicole", "Ian", "Bianca", 23, 21, 18, 16)

lista1 = ["Brendan", "Nicole", "Ian", "Bianca", 23, 21, 18, 16]
lista2 = [23, 21, 18, 16, 5, 200, 28000, 32, 55, 100]

#len devuelve la cantidad de elementos de la lista len()

lista = list(["Brendan", "Nicole", "Ian", "Bianca", 23, 21, 18, 16])
 
#agregando elementos con append
lista1.append("Willy")

#agregando un elemento en el index indicado colocando (posicion, "elemento")
lista1.insert(0, "Yanuri")

#agregando varios elemetos con extend4
lista1.extend(["Roberth", 30])

#Eliminando elementos con pop()
lista1.append("Guillermo")

#len cuenta los elementos de una lista desde el 1 
#Para eliminar elementos de derecha a izquierda se usa -1 para el ultimo elemento -2 para penultimo y asi sucesivamente

lista1.pop(-1)

#Remueve un elemento por su valor remove(valor)
lista1.remove(30)
print(lista1)
print(len(lista1))
#Eliminar todos los elementos de una lista Lista.clear()

#Ordenar la lista numerica incluyendo True y False de menor a mayor ( Usando el parametro reverse=True podemos darle vuelta al orden haciendo de mayor a menor)
lista2.sort()
print(lista2)
lista2.sort(reverse=True)
print(lista2)
#Revertir cualquier lista con lista.reverse()
lista2.reverse()
print(lista2)

idex_encontrado = lista1.index("Brendan")
print(idex_encontrado)