import flet as f

#Nombre cliente
#Numero de productos el que se lleve

def main(page: f.Page):
    page.title="Lista de la compra"
    t = f.Text(value="Fruterias Chen", color="blue",size=66,style="New york times")
    t.value="Fruterias Chen"
    page.add(t)
    textField_Nombre = f.TextField(label="Nombre",hint_text="Nombre")
    page.add(textField_Nombre)
    textField_Apellido = f.TextField(label="Apellido",hint_text="Apellido")
    page.add(textField_Apellido)
    dropDown_Menu = f.Dropdown(width=300,options=[f.dropdown.Option("L")])
    page.add(dropDown_Menu)
    dropDown_Menu.options.append(f.dropdown.Option("Nueva"))
    page.update()



f.app(target=main)