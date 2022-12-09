import flet as f

#Nombre cliente
#Numero de productos el que se lleve

def main(page: f.Page):
    page.title="Lista de la compra"
    t = f.Text(value="Fruterias Chen", color="blue",size=66)
    t.value="Fruterias Chen"
    page.add(t)




f.app(target=main)