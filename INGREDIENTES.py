import flet as f

#Nombre cliente
#Numero de productos el que se lleve

def main(page: f.Page):
    vusuario_alimento = []
    def usuario_alimento(e):
        vusuario_alimento.append(dropDown_Menu_verduras.value)
        vusuario_alimento.append(dropDown_Menu_frutas.value)
        print(vusuario_alimento)
    
    bt = f.FloatingActionButton(icon=f.icons.ADD, on_click=usuario_alimento)
    page.add(bt)



    page.title="Lista de la compra"
    t = f.Text(value="Fruterias Chen", color="blue",size=66)
    t.value="Fruterias Chen"
    page.add(t)
    textField_Nombre = f.TextField(label="Nombre",hint_text="Nombre")
    page.add(textField_Nombre)
    textField_Apellido = f.TextField(label="Apellido",hint_text="Apellido")
    page.add(textField_Apellido)
    tfrutas = f.Text(value="Frutas:",color="green",size=33)
    page.add(tfrutas)
    dropDown_Menu_frutas = f.Dropdown(width=300,options=[f.dropdown.Option("Peras")])
    page.add(dropDown_Menu_frutas)
    dropDown_Menu_frutas.options.append(f.dropdown.Option("Manzana"))
    dropDown_Menu_frutas.options.append(f.dropdown.Option("Naranjas"))
    dropDown_Menu_frutas.options.append(f.dropdown.Option("Fresas"))
    dropDown_Menu_frutas.options.append(f.dropdown.Option("Platano"))
    tfrutas_cantidad_slider = f.Slider(min=0,max=5000,divisions=5000,label="Cantidad{value}")
    page.add(tfrutas_cantidad_slider)
    tverduras = f.Text(value="Verduras",color="green",size=33)
    page.add(tverduras)
    dropDown_Menu_verduras = f.Dropdown(width=300,options=[f.dropdown.Option("Guisantes")])
    page.add(dropDown_Menu_verduras)
    dropDown_Menu_verduras.options.append(f.dropdown.Option("Cebollas"))
    dropDown_Menu_verduras.options.append(f.dropdown.Option("Lechuga"))
    dropDown_Menu_verduras.options.append(f.dropdown.Option("Alcachofa"))
    dropDown_Menu_verduras.options.append(f.dropdown.Option("Espárragos"))
    tverduras_cantidad_slider = f.Slider(min=0, max=5000, divisions=5000, label="Cantidad{value}")
    page.add(tverduras_cantidad_slider)




    page.update()







f.app(target=main)