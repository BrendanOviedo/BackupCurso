#Promedio de duracion cursos
Otros_cursos_min = 2.5
Otros_cursos_max = 7
Otros_cursos_promedio = 4
Este_curso = 1.5
#Crudos de los cursos
Crudo_promedio = 5
Crudo_Dalto = 3.5
#Calculo de tiempo
Diferencia_con_min = 100 - (Este_curso / Otros_cursos_min * 100) 
Diferencia_con_max = 100 - (Este_curso * 1000 // Otros_cursos_max / 10) 
Diferencia_con_promedio = 100 - (Este_curso / Otros_cursos_promedio * 100) 
#Calculo de crudo
Crudo_promedio1 = 100 - (Otros_cursos_promedio / Crudo_promedio * 100) 
Crudo_Dalto1 = 100 - (Este_curso * 1000 // Crudo_Dalto / 10)
#Calculo diferencias
Promedio_Horas_Diferencia = (Otros_cursos_promedio *100 // Este_curso / 10) 
Promedio_Horas_Diferencia_Dalto = (Este_curso *100 // Otros_cursos_promedio / 10)
print("------------------------------------------------")

print(" El curso de Dalto dura: ")
print(f" El curso dura {Diferencia_con_min}% menos que el mas rapido")
print(f" El curso dura {Diferencia_con_max}% menos que el mas lento")
print(f" El curso dura {Diferencia_con_promedio}% menos que el promedio")

print("------------------------------------------------")

print(" Los cursos eliminan: ")
print(f" Otros cursos eliminan el {Crudo_promedio1}% del material crudo")
print(f" Este curso elimina el {Crudo_Dalto1}% del material crudo")
print("------------------------------------------------")

print(" A cuanto equivalen las horas vistas entre los cursos: ")
print(f' Ver 10 horas de este curso equivale a ver {Promedio_Horas_Diferencia} horas de otros cursos')
print(f' Ver 10 horas de otros cursos equivale a ver {Promedio_Horas_Diferencia_Dalto} horas de este curso')

print("------------------------------------------------")