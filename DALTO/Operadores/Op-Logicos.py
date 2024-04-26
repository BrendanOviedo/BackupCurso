#controladores logicos and (&) or (|) not (not true/false)

#AND

resultado1 = True & True  #Devuelve True
resultado2 = False & True  #Devuelve False
resultado3 = True & False
resultado4 = False & False

#OR

resultado5 = True | True  #Devuelve True
resultado6 = True | False 
resultado7 = False | True
resultado8 = False | False #Devuelve False

#NOT

resultado9 = not True #Devuelve False
resultado10 = not False #Devuelve True 
resultado11 = not 2 == 4
print(resultado11) 