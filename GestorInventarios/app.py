import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, Toplevel
import json

def cargar_inventario():
    try:
        with open('inventario.json', 'r') as f:
            inventario = json.load(f)
        return inventario
    except FileNotFoundError:
        return {
            "Dato Prueba": {"cantidad": 10, "precio": 15},
            
        }

def guardar_inventario(inventario):
    with open('inventario.json', 'w') as f:
        json.dump(inventario, f)

carrito = []
total_venta = 0

def cambiar_precio():
    libro = simpledialog.askstring("Cambiar Precio", "Ingrese el nombre del libro para cambiar el precio:")
    if libro in inventario:
        nuevo_precio = simpledialog.askinteger("Nuevo Precio", "Ingrese el nuevo precio del libro:", minvalue=1)
        if nuevo_precio is not None:
            inventario[libro]['precio'] = nuevo_precio
            guardar_inventario(inventario)
            messagebox.showinfo("Precio Actualizado", f"El precio de '{libro}' ha sido actualizado a ₡{nuevo_precio}.")
        else:
            messagebox.showwarning("Operación Cancelada", "No se ha cambiado el precio.")
    else:
        messagebox.showerror("Error", "El libro no existe en el inventario.")

def eliminar_libro():
    libro = simpledialog.askstring("Eliminar Libro", "Ingrese el nombre del libro para eliminar:")
    if libro in inventario:
        if messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de que desea eliminar '{libro}' del inventario?"):
            del inventario[libro]
            guardar_inventario(inventario)
            combo_libros['values'] = list(inventario.keys())  # Actualizar el combobox
            messagebox.showinfo("Libro Eliminado", f"'{libro}' ha sido eliminado del inventario.")
        else:
            messagebox.showinfo("Operación Cancelada", "No se ha eliminado ningún libro.")
    else:
        messagebox.showerror("Error", "El libro no existe en el inventario.")

def actualizar_entry(event):
    libro_entry.delete(0, tk.END)
    libro_entry.insert(0, combo_libros.get())

def vender_libro():
    global total_venta
    libro = libro_entry.get()
    if libro and libro in inventario:
        cantidad_venta = simpledialog.askinteger("Cantidad", "Número de libros a vender:", minvalue=1, maxvalue=inventario[libro]["cantidad"])
        if cantidad_venta is not None:
            if inventario[libro]["cantidad"] >= cantidad_venta:
                inventario[libro]["cantidad"] -= cantidad_venta
                total_venta += inventario[libro]["precio"] * cantidad_venta
                carrito.append(f"{cantidad_venta} x {libro}")
                guardar_inventario(inventario)
                libro_entry.delete(0, tk.END)
                combo_libros.set('')
            else:
                messagebox.showerror("Error", "No hay suficientes unidades en el inventario.")
        else:
            messagebox.showwarning("Venta cancelada", "No se ha realizado ninguna venta.")
    else:
        messagebox.showerror("Error", "Seleccione un libro del menú desplegable o escriba uno válido.")

def agregar_libro():
    libro = simpledialog.askstring("Agregar libro", "Nombre del libro:")
    if libro is not None:
        cantidad = simpledialog.askinteger("Cantidad", "Número de libros a añadir:", minvalue=1)
        if cantidad is not None:
            if libro in inventario:
                inventario[libro]["cantidad"] += cantidad
            else:
                precio = simpledialog.askinteger("Precio", "Precio del libro:", minvalue=1, maxvalue=1000000)
                inventario[libro] = {"cantidad": cantidad, "precio": precio}
            guardar_inventario(inventario)
            combo_libros['values'] = list(inventario.keys())  # Actualizar el combobox
            messagebox.showinfo("Libro agregado", f"Añadidas {cantidad} unidades de '{libro}'.")
        else:
            messagebox.showwarning("Operación cancelada", "No se ha agregado ningún libro.")

def mostrar_inventario():
    def filtrar_inventario():
        filtro = busqueda_var.get().lower()
        libros_filtrados = "\n".join(f"{libro}: {datos['cantidad']} unidades, ₡{datos['precio']}"
                                     for libro, datos in inventario.items() if filtro in libro.lower())
        texto_inventario.config(state='normal')
        texto_inventario.delete(1.0, tk.END)
        texto_inventario.insert(tk.END, libros_filtrados)
        texto_inventario.config(state='disabled')

    ventana_inventario = Toplevel(root)
    ventana_inventario.title("Inventario de Libros")
    ventana_inventario.geometry("600x400")
    ventana_inventario.configure(bg='#333333')

    busqueda_var = tk.StringVar()
    busqueda_entry = tk.Entry(ventana_inventario, textvariable=busqueda_var, width=40, bg='#555555', fg='#FFFFFF')
    busqueda_entry.pack(pady=(10, 0))

    buscar_btn = tk.Button(ventana_inventario, text="Buscar", command=filtrar_inventario, bg=button_color, fg=button_text_color, font=button_font)
    buscar_btn.pack(pady=10)

    texto_inventario = tk.Text(ventana_inventario, height=20, width=100, bg='#333333', fg='#FFFFFF')
    texto_inventario.pack(pady=10)
    texto_inventario.config(state='disabled')

    # Mostrar todo el inventario inicialmente
    filtrar_inventario()

def finalizar_venta():
    global total_venta
    if not carrito:
        messagebox.showinfo("Carrito vacío", "No se han vendido libros.")
        return
    ventana_venta = Toplevel(root)
    ventana_venta.title("Libros Vendidos")
    ventana_venta.geometry("300x300")
    ventana_venta.configure(bg='#333333')
    texto_venta = tk.Text(ventana_venta, height=15, width=40, bg='#333333', fg='#FFFFFF')
    texto_venta.pack(pady=20)
    venta_resumen = "\n".join(carrito)
    venta_resumen += f"\n\nTotal: ₡{total_venta}"
    texto_venta.insert(tk.END, venta_resumen)
    texto_venta.config(state='disabled')
    carrito.clear()
    total_venta = 0

#Sistema Gui Base
inventario = cargar_inventario()

root = tk.Tk()
root.title("Gestor de Inventario de Librería")
root.geometry("500x450")
root.configure(bg='#333333')

default_font = ('Arial', 12)
button_font = ('Arial', 10, 'bold')
bg_color = '#333333'
text_color = '#FFFFFF'
button_color = '#555555'
button_text_color = '#FFFFFF'

combo_libros = ttk.Combobox(root, values=list(inventario.keys()), state='readonly')
combo_libros.pack(pady=10)
combo_libros.bind('<<ComboboxSelected>>', actualizar_entry)

#Botones

libro_entry = tk.Entry(root, width=50, bg='#555555', fg=text_color)
libro_entry.pack()

inventario_btn = tk.Button(root, text="Mostrar inventario", command=mostrar_inventario, bg=button_color, fg=button_text_color, font=button_font)
inventario_btn.pack(pady=10)

venta_btn = tk.Button(root, text="Agregar libro a venta", command=vender_libro, bg=button_color, fg=button_text_color, font=button_font)
venta_btn.pack(pady=10)

cambiar_precio_btn = tk.Button(root, text="Cambiar Precio de Libro", command=cambiar_precio, bg=button_color, fg=button_text_color, font=button_font)
cambiar_precio_btn.pack(pady=10)

agregar_btn = tk.Button(root, text="Agregar libro al inventario", command=agregar_libro, bg=button_color, fg=button_text_color, font=button_font)
agregar_btn.pack(pady=10)

eliminar_btn = tk.Button(root, text="Eliminar Libro del Inventario", command=eliminar_libro, bg=button_color, fg=button_text_color, font=button_font)
eliminar_btn.pack(pady=10)

finalizar_btn = tk.Button(root, text="Finalizar venta y mostrar resumen", command=finalizar_venta, bg=button_color, fg=button_text_color, font=button_font)
finalizar_btn.pack(pady=10)

root.mainloop()

