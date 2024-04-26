#abriendo el archivo con with open
with open("Archivos\\Texto.txt", encoding="UTF-8") as archivo:
    contenido_del_archivo = archivo.read()
    
    print(contenido_del_archivo)
#No es necesario cerrar el archivo con with
