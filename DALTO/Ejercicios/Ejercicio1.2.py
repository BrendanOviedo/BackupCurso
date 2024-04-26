
promedio_palabras_min = 2

frase = input("Escribe una frase y calculare cuanto tardarias en decirla: ") 
palabras_seperadas = frase.split(" ")
cantidad_de_palabras = len(palabras_seperadas)
Resultado1 = cantidad_de_palabras / 2 
Resultado2 = 30 * Resultado1 / 100
Resultado3 = Resultado1 - Resultado2
print(f"Dijiste {cantidad_de_palabras} palabras y tardarias en decirlo {cantidad_de_palabras / 2} segundos")
print(f"Dalto tardaria {Resultado3:.2f} segundos")

