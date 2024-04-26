#Diccionario con dict()
diccionario = dict(nombre = 'Brendan', apellido = 'Oviedo', edad = '')

#Las listas no pueden ser claves y usmos frozenset para meter conjuntos
diccionario = {frozenset(['dalto', "brendan"]):'hola perro'}

#Crear diccionrio con fromkeys() con dos parametros cambiando el valor por defecto a Sin Registro
diccionario = dict.fromkeys(['nombre', 'apellido'], "Sin Registro")
#Creando dict() con fromkey valor base "none"
diccionario = dict.fromkeys(['nombre', 'apellido'])
print(diccionario)

