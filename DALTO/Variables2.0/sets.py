#Creando conjunto frozenset

Conjunto = frozenset(["datos1", "datos2"])

#Meter un conjunto en otro se hace convierte el conjunto principal en conjunto fronzenset conviertienedolo en inalterable y asi pudiedo meter otros conjuntos

Conjunto1 = {Conjunto, "datos3"}

print(Conjunto1)

#Teoria de conjuntos 

conjunto2 = {1, 2, 3, 4, 5}
conjunto3 = {1, 4, 5}


#Verfiricar si es un subconjunto.

resultado = conjunto3.issubset(conjunto2)
resultado2 = conjunto3 <= conjunto2

#Verficiar si es un superconjunto

resultado3 = conjunto2.issuperset(conjunto3)
resultado4 = conjunto2 > conjunto3

#Averriguar si un dato en comun da false si es igual true si son diferentes
resultado5 = conjunto3.isdisjoint(conjunto2)
print(resultado5)
