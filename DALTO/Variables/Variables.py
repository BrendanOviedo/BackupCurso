#Definiendo una variable
Nombre = "Ian"
Nombre = "Brendan"
Nombre = "Bianca"
print(Nombre)

numero = 10
numero += 1
print(numero)

#Concatenar con +

bienvenida = "Hola " + Nombre + " como estas?"
print(bienvenida)

#Concatenar con f-strings

bienvenida1 = f"Hola {Nombre} Como estas?"
print(bienvenida1)

#Se puede utilizar f-strings para colocar comas despues del primer digito de numers=os altos con = (f"{x:,}")
#Se puede utilizar f-strings para reducir los decimales de un resultado con = (f"{x:.#dedecimalesf}")
#operadores de pertenencia (in or not in) para revisar si existen datos
print("Bianca" in bienvenida) #True
print("Bianca" not in bienvenida) #False

#Definir variables con CamelCase
NombreConCamelCase = "Brendan"
#Definir con Snake
Nombre_Con_Snake = "Brendan"