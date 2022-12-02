import flet as f


def main(page: f.Page):
    def cambiarColor(e):
        for i in range(11):
            text = f.Text(value=f"Texto numero {i}",size=30)
            page.add(text)

    #Componente texto 
    t = f.Text(value="Introducción a Flet", color="blue",size=66)
    page.add(t) #Add hace dos cosas 1- Añadir 2- Actualizar
    t.value="Cambiando los datos"
    #Actualiza los datos: page.update()
    #Componente boton
    bt = f.FloatingActionButton(icon=f.icons.ADD, on_click=cambiarColor)
    page.add(bt)

f.app(target=main)