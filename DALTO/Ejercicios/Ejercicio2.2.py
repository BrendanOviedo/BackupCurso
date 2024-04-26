#Crear funcion que devuelva los numeros primos 
#entre el 0 y el numero que le pasamos

def es_primo(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(2,num-1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos
resultado = primos_hasta(25)
print(resultado)
    