#pedir edad de los asistentes y acomodar de menor a mayor
#El mayor es el profesor y el menor el asistente
def obt_companeros(c_companeros):
    companeros = []
    for i in range(c_companeros):
        nombre = input("Nombre del companero: ")
        edad = int(input("Edad del companero: "))
        companero = (nombre, edad)
        companeros.append(companero)
    companeros.sort(key = lambda x:x[1])
    asistente = companeros[0][0]
    profesor = companeros [-1][0]
    return asistente, profesor

asistente, profesor = obt_companeros(3)
print(f"El profesor es {profesor} y el asistente es {asistente}")