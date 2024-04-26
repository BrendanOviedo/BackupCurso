diccionario = {
    'Nombre': 'Brendan',
    'Apellido': 'Oviedo',
    'edad': 23

}
#Recorriendo diccionario retornando solo claves
for clave in diccionario:
    print(clave)



#Recorriendo diccionario con items y retonando valor
for clave in diccionario.items():
     key = (clave[0])
     value = (clave[1])
     print(f"La clave es {key} y el valor es {value}")

