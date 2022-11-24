from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Iniciar sesión")
ventana.geometry("700x500")
ventana.resizable(False,False)
ventana.config(background="snow3")

label_titulo = ttk.Label(ventana,text="Datos usuario")

entry_nombre_usuario = ttk.Entry(ventana)
label_nombre_usuario = ttk.Label(ventana,text="Nombre usuario:")

label_pass_usuario = ttk.Label(ventana,text="Contraseña:")
entry_pass_usuario = ttk.Entry(ventana)

label_repite_pass_usuario = ttk.Label(ventana,text="Confirma contraseña")
entry_repite_pass_usuario = ttk.Entry(ventana)

boton_guardar = ttk.Button(ventana,text="Guardar")
boton_salir = ttk.Button(ventana,text="Salir")

#Pintar en pantalla los componentes
label_titulo.grid(row=0,column=1)
label_nombre_usuario.grid(row=1, column=0)
entry_nombre_usuario.grid(row=1, column=1)

label_pass_usuario.grid(row=2,column=0)
entry_pass_usuario.grid(row=2,column=1)

label_repite_pass_usuario.grid(row=3,column=0)
entry_repite_pass_usuario.grid(row=3,column=1)

boton_guardar.grid(row=5,column=0)
boton_salir.grid(row=5,column=1)








ventana.mainloop()