#while loops

#interger = 0
#while interger <= 2:
    #print("Meow")
#    interger += 1
    
#for loop range(#) devuelve la cantidad en el rango especificado se usa _ si no es necesario luego, por lo que se vuelve una variable sin nombre
#for _ in [0, 1, 2,]:
#    print("Meow")

#Compactar y conseguir el mismo resultado
#print("Meow\n" * 3, end="") 

#While loop usando range() y break
#while  True:
#    n = int(input("What's x?: "))
#    if n > 0:
#        break
    
#for _ in range(n):
#    print("Meow")

#students = ["Hermione", "Harry", "Ron"]

#for student in students:
#    print(student)
    
#for i in range(len(students)):
#    print(i + 1, students[i])

diccionario = {
    "Griffindor": ["Harry", "Ron", "Hermione"],
    "Slytherin": ["Draco", ]  
}

for student in diccionario.items():
    key = student[0]
    value = student[1]
    print(f"{key}, {value}")