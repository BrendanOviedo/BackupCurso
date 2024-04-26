#Creando funcion simple

def saludar():
    print("Hola mundo")

#ejecutando la funcion simple
#saludar()

def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "Titan"
    else :
        adjetivo = "Indefinido"
        
    print(f"Hola {nombre} como estas {adjetivo}")

#crear funcion que retorna valores

def crear_contrasena_random(num):
    chars = "abcdefghijkmlnopqrstuvwxyz"
    numero_entero = str(num)
    num = int(numero_entero[0])
    cl = num - 2
    cl2 = num 
    cl3 = num - 5
    contrasena = f'{chars[cl]}{chars[cl2]}{chars[cl3]}{num * 50}'
    return contrasena
    
resultado = crear_contrasena_random(int(input("Inserte numero: ")))
print(resultado)


