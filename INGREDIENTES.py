import flet as f

#Nombre cliente
#Numero de productos el que se lleve

def main(page: f.Page):
    vusuario_alimento = []
    def usuario_alimento(e):
        vusuario_alimento.append(textField_Nombre.value)
        vusuario_alimento.append(textField_Apellido.value)
        vusuario_alimento.append(dropDown_Menu_verduras.value)
        vusuario_alimento.append(tverduras_cantidad_slider.value)
        vusuario_alimento.append(dropDown_Menu_frutas.value)
        vusuario_alimento.append(tfrutas_cantidad_slider.value)
        vusuario_alimento.append(dropDown_Menu_carne.value)
        vusuario_alimento.append(tcarne_cantidad_slider.value)
        print(vusuario_alimento)
        textField_Nombre.value = ""
        textField_Apellido.value = ""
        dropDown_Menu_verduras.value = ""
        tverduras_cantidad_slider.value = 0
        dropDown_Menu_frutas.value = ""
        tfrutas_cantidad_slider.value = 0
        dropDown_Menu_carne.value = ""
        tcarne_cantidad_slider.value = 0
        
        
        page.update()

        
    page.scroll = "adaptive"

    
    
    page.title="Lista de la compra"
    t = f.Text(value="Lista de la compra", color="blue",size=66)
    t.value="Lista de la compra"
    page.add(t)
    textField_Nombre = f.TextField(label="Nombre",hint_text="Nombre")
    page.add(textField_Nombre)
    textField_Apellido = f.TextField(label="Apellido",hint_text="Apellido")
    page.add(textField_Apellido)
    
    tfrutas = f.Text(value="Frutas:",color="green",size=33)
    page.add(tfrutas)
    dropDown_Menu_frutas = f.Dropdown(width=300,options=[f.dropdown.Option("Peras")],label="Frutas")
    page.add(dropDown_Menu_frutas)
    page.add(f.Image(src=f"https://images.ecestaticos.com/Ga4J0tnBfGQNs25wDMmWOHnaThE=/1x110:2120x1302/1200x675/filters:fill(white):format(jpg)/f.elconfidencial.com%2Foriginal%2Ffa0%2Ff15%2Fc6a%2Ffa0f15c6a31a2eed9a19d7cba2c8b6d9.jpg",width=500,height=500))
    dropDown_Menu_frutas.options.append(f.dropdown.Option("Manzana"))
    dropDown_Menu_frutas.options.append(f.dropdown.Option("Naranjas"))
    dropDown_Menu_frutas.options.append(f.dropdown.Option("Fresas"))
    dropDown_Menu_frutas.options.append(f.dropdown.Option("Platano"))
    tfrutas_cantidad_slider = f.Slider(min=0,max=5000,divisions=5000,label="Gramos{value}")
    page.add(tfrutas_cantidad_slider)
    
    tverduras = f.Text(value="Verduras",color="green",size=33)
    page.add(tverduras)
    dropDown_Menu_verduras = f.Dropdown(width=300,options=[f.dropdown.Option("Guisantes")],label="Verduras")
    page.add(dropDown_Menu_verduras)
    page.add(f.Image(src=f"https://images.ecestaticos.com/-lvjpJLJluki4Zj7bXKJWC9Tiso=/130x25:676x434/1200x898/filters:fill(white):format(jpg)/f.elconfidencial.com%2Foriginal%2Fb25%2F568%2Fb4f%2Fb25568b4fdd2ab303a931ae702ebf800.jpg",width=500,height=500))
    
    dropDown_Menu_verduras.options.append(f.dropdown.Option("Cebollas"))
    dropDown_Menu_verduras.options.append(f.dropdown.Option("Lechuga"))
    dropDown_Menu_verduras.options.append(f.dropdown.Option("Alcachofa"))
    dropDown_Menu_verduras.options.append(f.dropdown.Option("Espárragos"))
    tverduras_cantidad_slider = f.Slider(min=0, max=5000, divisions=5000, label="Gramos{value}")
    page.add(tverduras_cantidad_slider)
    
    tcarne = f.Text(value="Carne:",color="green",size=33)
    page.add(tcarne)
    dropDown_Menu_carne = f.Dropdown(width=300,options=[f.dropdown.Option("Porcina")],label="Carnes")
    page.add(dropDown_Menu_carne)
    page.add(f.Image(src=f"https://static2.abc.es/media/bienestar/2021/09/27/tipos-de-carne-1-kWj--620x349@abc.jpg",width=500,height=500))
    dropDown_Menu_carne.options.append(f.dropdown.Option("Ovina"))
    dropDown_Menu_carne.options.append(f.dropdown.Option("Ternera"))
    dropDown_Menu_carne.options.append(f.dropdown.Option("Pollo"))
    dropDown_Menu_carne.options.append(f.dropdown.Option("Bóvida"))
    tcarne_cantidad_slider = f.Slider(min=0, max=5000, divisions=5000, label="Gramos{value}")
    page.add(tcarne_cantidad_slider)
    bt = f.TextButton("Añadir lista",icon="", on_click=usuario_alimento)
    page.add(bt)

    
    page.update()






f.app(target=main)
