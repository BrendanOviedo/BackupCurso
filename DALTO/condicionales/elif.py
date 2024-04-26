#if anidados y elif

ingreso_mensual = 100000
gasto_mensual = 10000
if ingreso_mensual >= 10000:
    if ingreso_mensual - gasto_mensual <= 0:
        print("Estamos en deficit")
    elif ingreso_mensual - gasto_mensual >= 5000:
        print("Estas bien pa")
    else:
        print("Estas gastando un huevo")    
    

elif ingreso_mensual >= 1000:
      print("Estas  bien economicamente")

else: 
    print("Sos pobreton")
           