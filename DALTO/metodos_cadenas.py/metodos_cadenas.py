cadena1 = "Hola Soy Brendan"
cadena2 = "PlayoIan"
cadena3 = "010305"
cadena4 = "a010305"
cadena5 = "Hola, buenas, tardes"
cadena6 = "Hola       Como Estas       ok"
#DIR es una funcion para averriguar los posibles comandos para el valor
resultado = dir(cadena1)

#Dato.Metodo() ejem. cadena1.upper()

#Upper() convierte a mayucula
#Lower() convierte a minuscula
#capitalize() convierte la frase a minuscula y convierte la primera letra a mayucula
#Buscamos una cadena en otra cadena 

#devuelve a mayuscula 
mayuscula = cadena1.upper()
#devuelve minuscula
minuscula = cadena1.lower()
#convierte toda la str a minuscula y luego la primera letra a mayucula
capit = cadena1.capitalize()
#convierte todas las primeras letras a mayuscula
title = cadena5.title()
#buscar una cadena en otra cadena devuelve -1 si no encuentra el valor
encontrar_find = cadena1.find("S")
#buscmos una cadena en otra cadena, si no hay coincidencia lanza error
encontrar_index = cadena1.index("S")
#si es numerico devuelve TRUE 
es_numerico = cadena3.isnumeric()
#Si es alfanumrico devuelve TRUE SOLO LETRAS DE LA A a LA Z, ES SENSIBLE A ESPACIOS Y CARACTERES ESPECIAALES
es_alfanumerico = cadena2.isalpha()
#Contar conincidencias funciona con alquier str
contar_coincidencias = cadena3.count("0")
#contar carcteres en una cadena, es sensible a espacios 
contar_caracteres = cadena1.__len__()
#Verfica si una cadena empieza con otra cadena dada
empiez_con = cadena1.startswith("Hola")
#Verifica si una cadena termiuna con otra cadena dada
term_con = cadena1.endswith("n")
#Si el valor 1 se encuestra en la cadena 1, se remplaza por el valor 2, si no es encontrado 
remplaza_con = cadena1.replace("la", "lu")
remplaza_con_2 = remplaza_con.capitalize()
#Separar cadenas con la cadena que le demos
separar_cadenas = cadena5.split(",")
#Elimina espacios en la cadena que le demos
limpiar_cadena = cadena6.strip
#Busca la cadena indicada dentro de otra, si no hay resultado no da error y entrega none

print(separar_cadenas[2])

