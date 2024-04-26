diccionario = {
    'Nombre' : 'Brendan',
    'Edad' : '23',
    'Altura' : '1.78',
    'Es_guapo' : True,
    'Gato' : 'Willy'
}

#Keys() Devuelve las claves del diccionario {Dict_item} (Se puede iterar)
claves = diccionario.keys()
#get() Devuelve el valor de una clave, si no es encontrado el valor no da error, sino que entrega "none"
Get = diccionario.get("Edad")
print("Dale pa")
#clear() Elimina todos los elementos
#diccionario.clear()
#pop() Elimina un elemento
diccionario.pop("Gato")
#items() Para itirar el dict Entrega la clave y su valor en conjunto (Clave, Valor)
diccionario_it = diccionario.items()



print(diccionario_it)


    