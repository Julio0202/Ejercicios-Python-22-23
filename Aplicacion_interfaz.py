from tkinter import *
from tkinter import ttk
from tkinter import messagebox
vlistas = []
usuario = ""
contrasena = ""
confirmarcontra = ""
def guardarDatos():
    usuario = entry_nombre_usuario.get()
    contrasena = entry_pass_usuario.get()
    confirmarcontra = entry_repite_pass_usuario.get()
    if contrasena == confirmarcontra:
        vlistas.append(usuario)
        vlistas.append(contrasena)
        entry_nombre_usuario.delete(0,len(usuario))
        entry_pass_usuario.delete(0,len(contrasena))
        entry_repite_pass_usuario.delete(0,len(confirmarcontra)) 
        messagebox.showinfo("Usuario Guardado", f"Usuario {usuario} guardado")
def listasDatos():
    print(vlistas)





ventana = Tk()
ventana.title("Iniciar sesión")
ventana.geometry("700x500")
ventana.resizable(False,False)
ventana.config(background="snow3")

label_titulo = ttk.Label(ventana,text="Datos usuario")

entry_nombre_usuario = ttk.Entry(ventana)
label_nombre_usuario = ttk.Label(ventana,text="Nombre usuario:")

label_pass_usuario = ttk.Label(ventana,text="Contraseña:")
entry_pass_usuario = ttk.Entry(ventana,show="*")

label_repite_pass_usuario = ttk.Label(ventana,text="Confirma contraseña")
entry_repite_pass_usuario = ttk.Entry(ventana,show="*")

boton_guardar = ttk.Button(ventana,text="Guardar",command=guardarDatos)
boton_salir = ttk.Button(ventana,text="Salir",command=ventana.destroy)

#Pintar en pantalla los componentes
label_titulo.grid(row=0,column=1)
label_nombre_usuario.grid(row=1, column=0, pady=10)
entry_nombre_usuario.grid(row=1, column=1, pady=10)

label_pass_usuario.grid(row=2,column=0, pady=10)
entry_pass_usuario.grid(row=2,column=1, pady=10)

label_repite_pass_usuario.grid(row=3,column=0, pady=10, padx=15)
entry_repite_pass_usuario.grid(row=3,column=1, pady=10)

boton_guardar.grid(row=5,column=0, pady=10)
boton_salir.grid(row=5,column=1, pady=10)








ventana.mainloop()