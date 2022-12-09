import flet as f


def main(page: f.Page):
    page.title="Flet inicio"
    def cambiar_color(e):
        t.value = textField_Nombre.value 
        page.update()
    #Componente texto 
    t = f.Text(value="Introducción a Flet", color="blue",size=66)
    page.add(t) #Add hace dos cosas 1- Añadir 2- Actualizar
    t.value="FLET < TKINTER, FACTS"
    page.update()
    #Actualiza los datos: page.update()
    #Componente boton
    bt = f.FloatingActionButton(icon=f.icons.ADD, on_click=cambiar_color)
    page.add(bt)
    textField_Nombre = f.TextField(label="Nombre",hint_text="Escribe tu nombre")
    page.add(textField_Nombre)
    dropDown_Menu = f.Dropdown(width=300,options=[f.dropdown.Option("L")])
    page.add(dropDown_Menu)
    dropDown_Menu.options.append(f.dropdown.Option("Nueva"))
    page.update()

    slider_edad=f.Slider(min=0,max=120,divisions=120,label="Edad{value}")
    page.add(slider_edad)
    #Crear fila
    fila = f.Row(controls=[textField_Nombre,dropDown_Menu])
    page.add(fila)
f.app(target=main)
