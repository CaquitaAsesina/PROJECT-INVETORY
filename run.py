from clase import Sistema
from tkinter import Button, Entry, Label, Tk, Frame, Canvas, Scrollbar, Toplevel
from PIL import Image, ImageTk

from cola import Cola
from fronted import interfaz_encolar, mostrar, interfaz_buscar_primero, interfaz_buscar_ultimo, interfaz_buscar_especifico, interfaz_eliminar_especifico, interfaz_error, interfaz_modificar
import random
cola = Cola()

#AGREGAR(SAVE)
def agregar_final(codigo, nombre, apellido, correo, telefono, categoria, ventana):
    if codigo == "" or nombre == "" or apellido == "" or correo == "" or telefono == "" or categoria == "":
        return interfaz_error("❌COMPLETA LOS DATOS❌")
    elif not codigo.isdigit():
        return interfaz_error("❌INGRESE DATOS BIEN❌")
    registro = Sistema(int(codigo), nombre, apellido, correo, int(telefono), categoria)
    usuario = cola.encolar(registro)
    if usuario == None:
        return interfaz_error("❌CODIDO DUPLICADO❌")
    ventana.destroy()
    return interfaz_encolar(usuario, usuario.getCodigo())

def comando_agregar():
    dic_nombres = [
    "Carlos Alberto",
    "Andrea Sofía",
    "Miguel Ángel",
    "Lucía Fernanda",
    "Jorge Ernesto",
    "Valeria Nicole",
    "Sebastián Daniel",
    "Camila Gabriela",
    "Bruno Alejandro",
    "Fiorella María"
    ] 
    dic_apellidos = [
    "Pérez Gonzales",
    "Ramos Torres",
    "Salazar Quispe",
    "Flores Lozano",
    "Vargas Rojas",
    "Mendoza Cáceres",
    "Sánchez Castillo",
    "Silva Morales",
    "Ruiz Delgado",
    "Cruz Herrera"
    ]
    dic_correo = [
    "skywave.contact@gmail.com",
    "nebula.systems@outlook.com",
    "byteflux.dev@hotmail.com",
    "stellarhub.info@gmail.com",
    "quantum.sync@protonmail.com",
    "darkpulse.data@gmail.com",
    "cyberlink.net@outlook.com",
    "nova.master.service@yahoo.com",
    "corestream.tech@gmail.com",
    "highpixel.cloud@outlook.com"
    ]
    dic_telefono = [
    "981245673",
    "927561408",
    "964781203",
    "912458730",
    "956701842",
    "934672810",
    "987310456",
    "945783210",
    "978640215",
    "923510478"
    ]
    dic_categoria = [
    "AMIGO",
    "FAMILIA",
    "TRABAJO"
    ]
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("430x430")
    ventana.configure(bg="#a3b1c6")
    titulo = Label(ventana, text="REGISTRAR USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#065A06", relief="groove", border=3)
    titulo.place(x=52, y=15, width=330, height=45)

    label_codigo = Label(ventana, text="CODIGO:", font=("impact", 16), bg="#9CC4A6", fg="#000000", relief="raised", border=5)
    label_codigo.place(x=15, y=70, width=140, height=40)
    entry_codigo = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_codigo.place(x=170, y=70, width=250, height=40)

    label_nombre= Label(ventana, text="NOMBRES:", font=("impact", 16), bg="#9CC4A6", fg="#000000", relief="raised", border=5)
    label_nombre.place(x=15, y=120, width=140, height=40)
    entry_nombre = Entry(ventana, font=("times", 14, "bold"), relief="solid", border=2)
    entry_nombre.place(x=170, y=120, width=250, height=40)
    entry_nombre.insert(0, random.choice(dic_nombres))

    label_apellido= Label(ventana, text="APELLIDOS:", font=("impact", 16), bg="#9CC4A6", fg="#000000", relief="raised", border=5)
    label_apellido.place(x=15, y=170, width=140, height=40)
    entry_apellido = Entry(ventana, font=("times", 14, "bold"), relief="solid", border=2)
    entry_apellido.place(x=170, y=170, width=250, height=40)
    entry_apellido.insert(0, random.choice(dic_apellidos))

    label_correo= Label(ventana, text="CORREO:", font=("impact", 16), bg="#9CC4A6", fg="#000000", relief="raised", border=5)
    label_correo.place(x=15, y=220, width=140, height=40)
    entry_correo = Entry(ventana, font=("times", 14, "bold"), relief="solid", border=2)
    entry_correo.place(x=170, y=220, width=250, height=40)
    entry_correo.insert(0, random.choice(dic_correo))

    label_telefono= Label(ventana, text="TELOFONO:", font=("impact", 16), bg="#9CC4A6", fg="#000000", relief="raised", border=5)
    label_telefono.place(x=15, y=270, width=140, height=40)
    entry_telefono = Entry(ventana, font=("times", 14, "bold"), relief="solid", border=2)
    entry_telefono.place(x=170, y=270, width=250, height=40)
    entry_telefono.insert(0, random.choice(dic_telefono))

    label_categoria= Label(ventana, text="CATEGORIA:", font=("impact", 16), bg="#9CC4A6", fg="#000000", relief="raised", border=5)
    label_categoria.place(x=15, y=320, width=140, height=40)
    entry_categoria = Entry(ventana, font=("times", 14, "bold"), relief="solid", border=2)
    entry_categoria.place(x=170, y=320, width=250, height=40)
    entry_categoria.insert(0, random.choice(dic_categoria))

    agregar = Button(ventana, text="AGREGAR USUARIO", command=lambda: (agregar_final(entry_codigo.get(), entry_nombre.get(), entry_apellido.get(), entry_correo.get(), entry_telefono.get(), entry_categoria.get(), ventana)), bg="#065A06", fg="#FFFFFF", font=("impact", 17), width=25, relief="groove", border=2)
    agregar.place(x=100, y=370, width=230, height=45)

#BUSCAR(SEARCH)
def comando_buscar_ultimo():
    usuario = cola.mostrar_ultimo()
    if usuario == None:
        return interfaz_error("❌NO HAY REGISTROS❌")
    return interfaz_buscar_ultimo(usuario)

def comando_buscar_primero():
    usuario = cola.mostrar_frente()
    if usuario == None:
        return interfaz_error("❌NO HAY REGISTROS❌")
    return interfaz_buscar_primero(usuario)

def buscar_codigo_final(codigo):
    codigo = codigo.strip()
    if codigo == "":
        return interfaz_error("❌COMPLETA LOS DATOS❌")
    elif not codigo.isdigit():
        return interfaz_error("❌NO USAR CARACTERES❌")
    usuario = cola.busca_codigo(int(codigo))
    if usuario == None:
        return interfaz_error("❌NO EXISTE EL CODIGO❌")
    return interfaz_buscar_especifico(usuario, "BUSQUEDA CODIGO")

def comando_buscar_codigo():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR CODIGO", font=("impact", 30), bg="#A1B7CF", fg="#0609BD", relief="groove", border=3)
    titulo.place(x=10, y=15, width=317, height=45)

    label_codigo = Label(ventana, text="CODIGO:", font=("impact", 16), bg="#8D8ED3", fg="#000000", relief="raised", border=5)
    label_codigo.place(x=15, y=70, width=140, height=40)

    entry_codigo = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_codigo.place(x=170, y=70, width=160, height=40)

    codigo_boton = Button(ventana, text="BUSCAR CODIGO", command=lambda: buscar_codigo_final(entry_codigo.get()), font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    codigo_boton.place(x=55, y=120, width=230, height=45)

def buscar_nombre_final(nombre):
    nombre   = nombre.strip()
    if nombre == "":
        return interfaz_error("❌COMPLETA LOS DATOS❌")
    if not nombre.replace(" ", "").isalpha():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.busca_nombre(nombre)
    if usuario == None:
        return interfaz_error("❌NO EXISTE EL NOMBRE❌")
    return interfaz_buscar_especifico(usuario, "BUSQUEDA NOMBRE")

def comando_buscar_nombre():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR NOMBRE", font=("impact", 30), bg="#A1B7CF", fg="#0609BD", relief="groove", border=3)
    titulo.place(x=10, y=15, width=317, height=45)

    label_nombre = Label(ventana, text="NOMBRE:", font=("impact", 16), bg="#8D8ED3", fg="#000000", relief="raised", border=5)
    label_nombre.place(x=15, y=70, width=140, height=40)

    entry_nombre = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_nombre.place(x=170, y=70, width=160, height=40)

    nombre_boton = Button(ventana, text="BUSCAR NOMBRE", command=lambda: buscar_nombre_final(entry_nombre.get()), font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    nombre_boton.place(x=55, y=120, width=230, height=45)
    
def buscar_apellido_final(apellido):
    apellido   = apellido.strip()
    if apellido == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if not apellido.replace(" ", "").isalpha():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.busca_apellido(apellido)
    if usuario == None:
        return interfaz_error("❌NO EXISTE EL APELLIDO❌")
    return interfaz_buscar_especifico(usuario, "BUSQUEDA APELLIDO")
    
def comando_buscar_apellido():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR APELLIDO", font=("impact", 30), bg="#A1B7CF", fg="#0609BD", relief="groove", border=3)
    titulo.place(x=10, y=15, width=317, height=45)

    label_apellido = Label(ventana, text="APELLIDO:", font=("impact", 16), bg="#8D8ED3", fg="#000000", relief="raised", border=5)
    label_apellido.place(x=15, y=70, width=140, height=40)

    entry_apellido = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_apellido.place(x=170, y=70, width=160, height=40)

    apellido_boton = Button(ventana, text="BUSCAR APELLLIDO", command=lambda: buscar_apellido_final(entry_apellido.get()), font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    apellido_boton.place(x=55, y=120, width=230, height=45)

def buscar_correo_final(correo):
    correo   = correo.strip()
    if correo == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if correo.isdigit():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.busca_correo(correo)
    if usuario == None:
        return interfaz_error("❌NO EXISTE EL CORREO❌")
    return interfaz_buscar_especifico(usuario, "BUSQUEDA CORREO")

def comando_buscar_correo():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR CORREO", font=("impact", 30), bg="#A1B7CF", fg="#0609BD", relief="groove", border=3)
    titulo.place(x=10, y=15, width=317, height=45)

    label_correo = Label(ventana, text="CORREO:", font=("impact", 16), bg="#8D8ED3", fg="#000000", relief="raised", border=5)
    label_correo.place(x=15, y=70, width=140, height=40)

    entry_correo = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_correo.place(x=170, y=70, width=160, height=40)

    correo_boton = Button(ventana, text="BUSCAR CORREO", command=lambda: buscar_correo_final(entry_correo.get()), font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    correo_boton.place(x=55, y=120, width=230, height=45)

def buscar_telefono_final(telefono):
    telefono   = telefono.strip()
    if telefono == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if not telefono.isdigit():
        return interfaz_error("❌NO USAR CARACTERES❌")
    usuario = cola.busca_telefono(int(telefono))
    if usuario == None:
        return interfaz_error("❌NO EXISTE EL TELEFONO❌")
    return interfaz_buscar_especifico(usuario, "BUSQUEDA TELEFONO")

def comando_buscar_telefono():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR TELEFONO", font=("impact", 30), bg="#A1B7CF", fg="#0609BD", relief="groove", border=3)
    titulo.place(x=10, y=15, width=317, height=45)

    label_telefono = Label(ventana, text="TELEFONO:", font=("impact", 16), bg="#8D8ED3", fg="#000000", relief="raised", border=5)
    label_telefono.place(x=15, y=70, width=140, height=40)

    entry_telefono = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_telefono.place(x=170, y=70, width=160, height=40)

    telefono_boton = Button(ventana, text="BUSCAR TELEFONO", command=lambda: buscar_telefono_final(entry_telefono.get()), font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    telefono_boton.place(x=55, y=120, width=230, height=45)
    
def buscar_categoria_final(categoria):
    categoria   = categoria.strip()
    if categoria == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if not categoria.replace(" ", "").isalpha():
        return interfaz_error("❌SOLO CARACTERES❌")
    registros = cola.busca_categoria(categoria)
    if registros == None:
        return interfaz_error("❌NO EXISTE LA CATEGORIA❌")
    return mostrar(registros, "🔍BUSCAR CATEGORIA🔎")
    
def comando_buscar_categoria():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR CATEGORIA", font=("impact", 30), bg="#A1B7CF", fg="#0609BD", relief="groove", border=3)
    titulo.place(x=10, y=15, width=317, height=45)

    label_categoria = Label(ventana, text="CATEGORIA:", font=("impact", 16), bg="#8D8ED3", fg="#000000", relief="raised", border=5)
    label_categoria.place(x=15, y=70, width=140, height=40)

    entry_categoria = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_categoria.place(x=170, y=70, width=160, height=40)

    categoria_boton = Button(ventana, text="BUSCAR CATEGORIA", command=lambda: buscar_categoria_final(entry_categoria.get()), font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    categoria_boton.place(x=55, y=120, width=230, height=45)

def comando_buscar_especifico():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x410")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#0609BD", relief="groove", border=3)
    titulo.place(x=20, y=15, width=300, height=45)

    buscar_codigo = Button(ventana, text="BUSCAR CODIGO", command=comando_buscar_codigo, font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    buscar_codigo.place(x=55, y=70, width=230, height=45)
    
    buscar_nombre = Button(ventana, text="BUSCAR NOMBRE", command=comando_buscar_nombre, font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    buscar_nombre.place(x=55, y=125, width=230, height=45)
    
    buscar_apellido = Button(ventana, text="BUSCAR APELLIDO", command=comando_buscar_apellido, font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    buscar_apellido.place(x=55, y=180, width=230, height=45)
    
    buscar_correo = Button(ventana, text="BUSCAR CORREO", command=comando_buscar_correo, font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    buscar_correo.place(x=55, y=235, width=230, height=45)
    
    buscar_telefono = Button(ventana, text="BUSCAR TELEFONO", command=comando_buscar_telefono, font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    buscar_telefono.place(x=55, y=290, width=230, height=45)
    
    buscar_categoria = Button(ventana, text="BUSCAR CATEGORIA", command=comando_buscar_categoria, font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    buscar_categoria.place(x=55, y=345, width=230, height=45)

def comando_buscar():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x240")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#0609BD", relief="groove", border=3)
    titulo.place(x=20, y=15, width=300, height=45)

    primero_boton = Button(ventana, text="BUSCAR PRIMERO", command=comando_buscar_primero, font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    primero_boton.place(x=55, y=70, width=230, height=45)

    ultimo_boton = Button(ventana, text="BUSCAR ULTIMO", command=comando_buscar_ultimo, font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    ultimo_boton.place(x=55, y=125, width=230, height=45)
    
    especifico_boton = Button(ventana, text="BUSCAR ESPECIFICO", command=comando_buscar_especifico, font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
    especifico_boton.place(x=55, y=180, width=230, height=45)

#ELIMINAR(DELETE)
def eliminar_primero_final():
    usuario = cola.desencolar()
    if usuario == None:
        return interfaz_error("❌OCURRIO UN PROBLEMA❌")
    return usuario

def comando_eliminar_primero():
    usuario = cola.mostrar_frente()
    if usuario == None:
        return interfaz_error("❌NO HAY REGISTROS❌")
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="PRIMER USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#990505", relief="groove", border=3)
    titulo.place(x=20, y=15, width=300, height=45)

    usuario= Label(ventana, text=usuario, font=("Segoe U", 10), bg="#ACBEF0", fg="#000000", relief="raised", border=2, justify= "left")
    usuario.place(x=35, y=70, width=270, height=215)

    eliminar = Button(ventana, text="ELIMINAR PRIMERO", command=eliminar_primero_final, font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    eliminar.place(x=55, y=295, width=220, height=45)

def eliminar_ultimo_final():
    usuario = cola.desencolar_ultimo()
    if usuario == None:
        return interfaz_error("❌OCURRIO UN PROBLEMA❌")
    return usuario

def comando_eliminar_ultimo():
    usuario = cola.mostrar_ultimo()
    if usuario == None:
        return interfaz_error("❌NO HAY REGISTROS❌")
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="ULTIMO USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#990505", relief="groove", border=3)
    titulo.place(x=20, y=15, width=300, height=45)

    usuario= Label(ventana, text=usuario, font=("Segoe U", 10), bg="#ACBEF0", fg="#000000", relief="raised", border=2, justify= "left")
    usuario.place(x=35, y=70, width=270, height=215)

    eliminar = Button(ventana, text="ELIMINAR ULTIMO", command=eliminar_ultimo_final, font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    eliminar.place(x=55, y=295, width=220, height=45)

def eliminar_codigo_final(codigo):
    if codigo == "":
        return interfaz_error("❌COMPLETA LOS DATOS❌")
    elif not codigo.isdigit():
        return interfaz_error("❌NO USAR CARACTERES❌")
    usuario = cola.eliminar_codigo(int(codigo))
    if usuario == None:
        return interfaz_error("❌NO EXISTE EL CODIGO❌")
    return interfaz_eliminar_especifico(usuario, "ELIMINAR CODIGO")

def comando_eliminar_codigo():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR CODIGO", font=("impact", 30), bg="#A1B7CF", fg="#990505", relief="groove", border=3)
    titulo.place(x=10, y=15, width=317, height=45)

    label_codigo = Label(ventana, text="CODIGO:", font=("impact", 16), bg="#D47878", fg="#000000", relief="raised", border=5)
    label_codigo.place(x=15, y=70, width=140, height=40)

    entry_codigo = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_codigo.place(x=170, y=70, width=160, height=40)

    codigo_boton = Button(ventana, text="ELIMINAR CODIGO", command=lambda: eliminar_codigo_final(entry_codigo.get()), font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    codigo_boton.place(x=55, y=120, width=230, height=45)

def eliminar_nombre_final(nombre):
    nombre = nombre.strip()
    if nombre == "":
        return interfaz_error("❌COMPLETA LOS DATOS❌")
    if not nombre.replace(" ", "").isalpha():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.eliminar_nombre(nombre)
    if usuario == None:
        return interfaz_error("❌NO EXISTE EL NOMBRE❌")
    return interfaz_eliminar_especifico(usuario, "ELIMINAR NOMBRE")

def comando_eliminar_nombre():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR NOMBRE", font=("impact", 30), bg="#A1B7CF", fg="#990505", relief="groove", border=3)
    titulo.place(x=10, y=15, width=317, height=45)

    label_nombre = Label(ventana, text="NOMBRE:", font=("impact", 16), bg="#D47878", fg="#000000", relief="raised", border=5)
    label_nombre.place(x=15, y=70, width=140, height=40)

    entry_nombre = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_nombre.place(x=170, y=70, width=160, height=40)

    nombre_boton = Button(ventana, text="ELIMINAR NOMBRE", command=lambda: eliminar_nombre_final(entry_nombre.get()), font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    nombre_boton.place(x=55, y=120, width=230, height=45)

def eliminar_apellido_final(apellido):
    apellido = apellido.strip()
    if apellido == "":
        return interfaz_error("❌COMPLETA LOS DATOS❌")
    if not apellido.replace(" ", "").isalpha():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.eliminar_apellido(apellido)
    if usuario == None:
        return interfaz_error("❌NO EXISTE EL APELLIDO❌")
    return interfaz_eliminar_especifico(usuario, "ELIMINAR APELLIDO")

def comando_eliminar_apellido():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR APELLIDO", font=("impact", 30), bg="#A1B7CF", fg="#990505", relief="groove", border=3)
    titulo.place(x=10, y=15, width=317, height=45)

    label_apellido = Label(ventana, text="APELLIDO:", font=("impact", 16), bg="#D47878", fg="#000000", relief="raised", border=5)
    label_apellido.place(x=15, y=70, width=140, height=40)

    entry_apellido = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_apellido.place(x=170, y=70, width=160, height=40)

    apellido_boton = Button(ventana, text="ELIMINAR APELLIDO", command=lambda: eliminar_apellido_final(entry_apellido.get()), font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    apellido_boton.place(x=55, y=120, width=230, height=45)

def eliminar_correo_final(correo):
    correo = correo.strip()
    if correo == "":
        return interfaz_error("❌COMPLETA LOS DATOS❌")
    if correo.isdigit():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.eliminar_correo(correo)
    if usuario == None:
        return interfaz_error("❌NO EXISTE EL CORREO❌")
    return interfaz_eliminar_especifico(usuario, "ELIMINAR CORREO")

def comando_eliminar_correo():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR CORREO", font=("impact", 30), bg="#A1B7CF", fg="#990505", relief="groove", border=3)
    titulo.place(x=10, y=15, width=317, height=45)

    label_correo = Label(ventana, text="CORREO:", font=("impact", 16), bg="#D47878", fg="#000000", relief="raised", border=5)
    label_correo.place(x=15, y=70, width=140, height=40)

    entry_correo = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_correo.place(x=170, y=70, width=160, height=40)

    correo_boton = Button(ventana, text="ELIMINAR CORREO", command=lambda: eliminar_correo_final(entry_correo.get()), font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    correo_boton.place(x=55, y=120, width=230, height=45)

def eliminar_telefono_final(telefono):
    telefono = telefono.strip()
    if telefono == "":
        return interfaz_error("❌COMPLETA LOS DATOS❌")
    elif not telefono.isdigit():
        return interfaz_error("❌NO USAR CARACTERES❌")
    usuario = cola.eliminar_telefono(int(telefono))
    if usuario == None:
        return interfaz_error("❌NO EXISTE EL TELEFONO❌")
    return interfaz_eliminar_especifico(usuario, "ELIMINAR TELEFONO")

def comando_eliminar_telefono():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR TELEFONO", font=("impact", 30), bg="#A1B7CF", fg="#990505", relief="groove", border=3)
    titulo.place(x=10, y=15, width=317, height=45)

    label_telefono = Label(ventana, text="TELEFONO:", font=("impact", 16), bg="#D47878", fg="#000000", relief="raised", border=5)
    label_telefono.place(x=15, y=70, width=140, height=40)

    entry_telefono = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_telefono.place(x=170, y=70, width=160, height=40)

    telefono_boton = Button(ventana, text="ELIMINAR TELEFONO", command=lambda: eliminar_telefono_final(entry_telefono.get()), font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    telefono_boton.place(x=55, y=120, width=230, height=45)

def eliminar_categoria_final(categoria):
    categoria = categoria.strip()
    if categoria == "":
        return interfaz_error("❌COMPLETA LOS DATOS❌")
    if not categoria.replace(" ", "").isalpha():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuarios = cola.eliminar_categoria(categoria)
    if usuarios == None:
        return interfaz_error("❌NO EXISTE LA CATEGORIA❌")
    return mostrar(usuarios, "ELIMINAR CATEGORIA")

def comando_eliminar_categoria():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="BUSCAR CATEGORIA", font=("impact", 30), bg="#A1B7CF", fg="#990505", relief="groove", border=3)
    titulo.place(x=10, y=15, width=317, height=45)

    label_categoria = Label(ventana, text="CATEGORIA:", font=("impact", 16), bg="#D47878", fg="#000000", relief="raised", border=5)
    label_categoria.place(x=15, y=70, width=140, height=40)

    entry_categoria = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_categoria.place(x=170, y=70, width=160, height=40)

    categoria_boton = Button(ventana, text="ELIMINAR CATEGORIA", command=lambda: eliminar_categoria_final(entry_categoria.get()), font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    categoria_boton.place(x=55, y=120, width=230, height=45)

def comando_eliminar_especifico():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x410")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="ELIMINAR USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#990505", relief="groove", border=3)
    titulo.place(x=20, y=15, width=300, height=45)

    eliminar_codigo = Button(ventana, text="ELIMINAR CODIGO", command=comando_eliminar_codigo, font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    eliminar_codigo.place(x=55, y=70, width=230, height=45)
    
    eliminar_nombre = Button(ventana, text="ELIMINAR NOMBRE", command=comando_eliminar_nombre, font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    eliminar_nombre.place(x=55, y=125, width=230, height=45)
    
    eliminiar_apellido = Button(ventana, text="ELIMINAR APELLIDO", command=comando_eliminar_apellido, font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    eliminiar_apellido.place(x=55, y=180, width=230, height=45)
    
    eliminiar_correo = Button(ventana, text="ELIMINAR CORREO", command=comando_eliminar_correo, font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    eliminiar_correo.place(x=55, y=235, width=230, height=45)
    
    eliminar_telefono = Button(ventana, text="ELIMINAR TELEFONO", command=comando_eliminar_telefono, font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    eliminar_telefono.place(x=55, y=290, width=230, height=45)
    
    eliminiar_boton = Button(ventana, text="ELIMINAR CATEGORIA", command=comando_eliminar_categoria, font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    eliminiar_boton.place(x=55, y=345, width=230, height=45)

def comando_eliminar():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x240")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="ELIMINAR USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#990505", relief="groove", border=3)
    titulo.place(x=20, y=15, width=300, height=45)

    primero_boton = Button(ventana, text="ELIMINAR PRIMERO", command=comando_eliminar_primero, font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    primero_boton.place(x=55, y=70, width=230, height=45)

    ultimo_boton = Button(ventana, text="ELIMINAR ULTIMO", command=comando_eliminar_ultimo, font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    ultimo_boton.place(x=55, y=125, width=230, height=45)
    
    especifico_boton = Button(ventana, text="ELIMINAR ESPECIFICO", command=comando_eliminar_especifico, font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
    especifico_boton.place(x=55, y=180, width=230, height=45)

#MODIFICAR(UPDATE) 
def modificar_primero_nombre_final(nombre):
    nombre = nombre.strip()
    if nombre == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if not nombre.replace(" ", "").isalpha():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.modificar_frente_nombre(nombre)
    if usuario == None:
        return interfaz_error("❌OCURRIO UN PROBLEMA❌")
    return interfaz_modificar(usuario, "NOMBRE MODIFICADO")

def modificar_primero_nombre():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="MODIFICAR NOMBRE", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=10, y=15, width=320, height=45)

    label_nombre = Label(ventana, text="NOMBRE:", font=("impact", 16), bg="#BA8FD6", fg="#000000", relief="raised", border=5)
    label_nombre.place(x=15, y=70, width=140, height=40)

    entry_nombre = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_nombre.place(x=170, y=70, width=160, height=40)

    nombre_boton = Button(ventana, text="MODIFICAR NOMBRE", command=lambda: modificar_primero_nombre_final(entry_nombre.get()), font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    nombre_boton.place(x=50, y=120, width=240, height=45)

def modificar_primero_apellido_final(apellido):
    apellido = apellido.strip()
    if apellido == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if not apellido.replace(" ", "").isalpha():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.modificar_frente_apellido(apellido)
    if usuario == None:
        return interfaz_error("❌OCURRIO UN PROBLEMA❌")
    return interfaz_modificar(usuario, "APELLIDO MODIFICADO")

def modificar_primero_apellido():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="MODIFICAR APELL.", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=10, y=15, width=320, height=45)

    label_apellido = Label(ventana, text="APELLIDO:", font=("impact", 16), bg="#BA8FD6", fg="#000000", relief="raised", border=5)
    label_apellido.place(x=15, y=70, width=140, height=40)

    entry_apellido = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_apellido.place(x=170, y=70, width=160, height=40)

    apellido_boton = Button(ventana, text="MODIFICAR APELLIDO", command=lambda: modificar_primero_apellido_final(entry_apellido.get()), font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    apellido_boton.place(x=50, y=120, width=240, height=45)

def modificar_primero_correo_final(correo):
    correo = correo.strip()
    if correo == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if correo.isdigit():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.modificar_frente_correo(correo)
    if usuario == None:
        return interfaz_error("❌OCURRIO UN PROBLEMA❌")
    return interfaz_modificar(usuario, "CORREO MODIFICADO")

def modificar_primero_correo():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="MODIFICAR CORREO", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=10, y=15, width=320, height=45)

    label_correo = Label(ventana, text="CORREO:", font=("impact", 16), bg="#BA8FD6", fg="#000000", relief="raised", border=5)
    label_correo.place(x=15, y=70, width=140, height=40)

    entry_correo = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_correo.place(x=170, y=70, width=160, height=40)

    correo_boton = Button(ventana, text="MODIFICAR CORREO", command=lambda: modificar_primero_correo_final(entry_correo.get()), font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    correo_boton.place(x=50, y=120, width=240, height=45)

def modificar_primero_telefono_final(telefono):
    telefono = telefono.strip()
    if telefono == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if not telefono.isdigit():
        return interfaz_error("❌NO CARACTERES❌")
    usuario = cola.modificar_frente_telefono(telefono)
    if usuario == None:
        return interfaz_error("❌OCURRIO UN PROBLEMA❌")
    return interfaz_modificar(usuario, "TELEFONO MODIFICADO")

def modificar_primero_telefono():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="MODIFICAR TELEF.", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=10, y=15, width=320, height=45)

    label_telefono = Label(ventana, text="TELEFONO:", font=("impact", 16), bg="#BA8FD6", fg="#000000", relief="raised", border=5)
    label_telefono.place(x=15, y=70, width=140, height=40)

    entry_telefono = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_telefono.place(x=170, y=70, width=160, height=40)

    telefono_boton = Button(ventana, text="MODIFICAR TELEFONO", command=lambda: modificar_primero_telefono_final(entry_telefono.get()), font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    telefono_boton.place(x=50, y=120, width=240, height=45)

def modificar_primero_categoria_final(categoria):
    categoria = categoria.strip()
    if categoria == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if not categoria.replace(" ", "").isalpha():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.modificar_frente_categoria(categoria)
    if usuario == None:
        return interfaz_error("❌OCURRIO UN PROBLEMA❌")
    return interfaz_modificar(usuario, "CATEGORIA MODIFICADA")

def modificar_primero_categoria():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="MODIFICAR CATEG.", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=10, y=15, width=320, height=45)

    label_categoria = Label(ventana, text="CATEGORIA:", font=("impact", 16), bg="#BA8FD6", fg="#000000", relief="raised", border=5)
    label_categoria.place(x=15, y=70, width=140, height=40)

    entry_categoria = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_categoria.place(x=170, y=70, width=160, height=40)

    categoria_boton = Button(ventana, text="MODIFICAR CATEGORIA", command=lambda: modificar_primero_categoria_final(entry_categoria.get()), font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    categoria_boton.place(x=50, y=120, width=240, height=45)

def modificar_primero_final():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="MODIFICAR USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=7, y=15, width=327, height=45)

    modifcar_nombre = Button(ventana, text="MODIFICAR NOMBRE", command=modificar_primero_nombre, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    modifcar_nombre.place(x=55, y=70, width=230, height=45)
    
    modificar_apellido = Button(ventana, text="MODIFICAR APELLIDO", command=modificar_primero_apellido, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    modificar_apellido.place(x=55, y=125, width=230, height=45)
    
    modificar_correo = Button(ventana, text="MODIFICAR CORREO", command=modificar_primero_correo, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    modificar_correo.place(x=55, y=180, width=230, height=45)
    
    modificar_telefono = Button(ventana, text="MODIFICAR TELEFONO", command=modificar_primero_telefono, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    modificar_telefono.place(x=55, y=235, width=230, height=45)
    
    modificar_categoria = Button(ventana, text="MODIFICAR CATEGORIA", command=modificar_primero_categoria, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    modificar_categoria.place(x=55, y=290, width=230, height=45)
    
def comando_modificar_primero():
    registro = cola.mostrar_frente()
    if registro == None:
        return interfaz_error("❌NO HAY REGISTROS❌")
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="PRIMER USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=25, y=15, width=290, height=45)

    usuario= Label(ventana, text=registro, font=("Segoe U", 10), bg="#ACBEF0", fg="#000000", relief="raised", border=2, justify= "left")
    usuario.place(x=35, y=70, width=270, height=215)

    modificar_boton = Button(ventana, text="MODIFICAR PRIMERO", command=modificar_primero_final, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    modificar_boton.place(x=55, y=295, width=230, height=45)

def modificar_ultimo_nombre_final(nombre):
    nombre = nombre.strip()
    if nombre == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if not nombre.replace(" ", "").isalpha():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.modificar_ultimo_nombre(nombre)
    if usuario == None:
        return interfaz_error("❌OCURRIO UN PROBLEMA❌")
    return interfaz_modificar(usuario, "NOMBRE MODIFICADO")

def modificar_ultimo_nombre():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="MODIFICAR NOMBRE", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=10, y=15, width=320, height=45)

    label_nombre = Label(ventana, text="NOMBRE:", font=("impact", 16), bg="#BA8FD6", fg="#000000", relief="raised", border=5)
    label_nombre.place(x=15, y=70, width=140, height=40)

    entry_nombre = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_nombre.place(x=170, y=70, width=160, height=40)

    nombre_boton = Button(ventana, text="MODIFICAR NOMBRE", command=lambda: modificar_ultimo_nombre_final(entry_nombre.get()), font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    nombre_boton.place(x=50, y=120, width=240, height=45)

def modificar_ultimo_apellido_final(apellido):
    apellido = apellido.strip()
    if apellido == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if not apellido.replace(" ", "").isalpha():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.modificar_ultimo_apellido(apellido)
    if usuario == None:
        return interfaz_error("❌OCURRIO UN PROBLEMA❌")
    return interfaz_modificar(usuario, "APELLIDO MODIFICADO")

def modificar_ultimo_apellido():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="MODIFICAR APELL.", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=10, y=15, width=320, height=45)

    label_apellido = Label(ventana, text="APELLIDO:", font=("impact", 16), bg="#BA8FD6", fg="#000000", relief="raised", border=5)
    label_apellido.place(x=15, y=70, width=140, height=40)

    entry_apellido = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_apellido.place(x=170, y=70, width=160, height=40)

    apellido_boton = Button(ventana, text="MODIFICAR APELLIDO", command=lambda: modificar_ultimo_apellido_final(entry_apellido.get()), font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    apellido_boton.place(x=50, y=120, width=240, height=45)

def modificar_ultimo_correo_final(correo):
    correo = correo.strip()
    if correo == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if correo.isdigit():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.modificar_ultimo_correo(correo)
    if usuario == None:
        return interfaz_error("❌OCURRIO UN PROBLEMA❌")
    return interfaz_modificar(usuario, "CORREO MODIFICADO")

def modificar_ultimo_correo():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="MODIFICAR CORREO", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=10, y=15, width=320, height=45)

    label_correo = Label(ventana, text="CORREO:", font=("impact", 16), bg="#BA8FD6", fg="#000000", relief="raised", border=5)
    label_correo.place(x=15, y=70, width=140, height=40)

    entry_correo = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_correo.place(x=170, y=70, width=160, height=40)

    correo_boton = Button(ventana, text="MODIFICAR CORREO", command=lambda: modificar_ultimo_correo_final(entry_correo.get()), font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    correo_boton.place(x=50, y=120, width=240, height=45)

def modificar_ultimo_telefono_final(telefono):
    telefono = telefono.strip()
    if telefono == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if not telefono.isdigit():
        return interfaz_error("❌NO CARACTERES❌")
    usuario = cola.modificar_ultimo_telefono(telefono)
    if usuario == None:
        return interfaz_error("❌OCURRIO UN PROBLEMA❌")
    return interfaz_modificar(usuario, "TELEFONO MODIFICADO")

def modificar_ultimo_telefono():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="MODIFICAR TELEF.", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=10, y=15, width=320, height=45)

    label_telefono = Label(ventana, text="TELEFONO:", font=("impact", 16), bg="#BA8FD6", fg="#000000", relief="raised", border=5)
    label_telefono.place(x=15, y=70, width=140, height=40)

    entry_telefono = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_telefono.place(x=170, y=70, width=160, height=40)

    telefono_boton = Button(ventana, text="MODIFICAR TELEFONO", command=lambda: modificar_ultimo_telefono_final(entry_telefono.get()), font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    telefono_boton.place(x=50, y=120, width=240, height=45)

def modificar_ultimo_categoria_final(categoria):
    categoria = categoria.strip()
    if categoria == "":
        return interfaz_error("❌COMPLETE LOS DATOS❌")
    if not categoria.replace(" ", "").isalpha():
        return interfaz_error("❌SOLO CARACTERES❌")
    usuario = cola.modificar_ultimo_categoria(categoria)
    if usuario == None:
        return interfaz_error("❌OCURRIO UN PROBLEMA❌")
    return interfaz_modificar(usuario, "CATEGORIA MODIFICADA")

def modificar_ultimo_categoria():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="MODIFICAR CATEG.", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=10, y=15, width=320, height=45)

    label_categoria = Label(ventana, text="CATEGORIA:", font=("impact", 16), bg="#BA8FD6", fg="#000000", relief="raised", border=5)
    label_categoria.place(x=15, y=70, width=140, height=40)

    entry_categoria = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_categoria.place(x=170, y=70, width=160, height=40)

    categoria_boton = Button(ventana, text="MODIFICAR CATEGORIA", command=lambda: modificar_ultimo_categoria_final(entry_categoria.get()), font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    categoria_boton.place(x=50, y=120, width=240, height=45)

def modificar_ultimo_final():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="MODIFICAR USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=7, y=15, width=327, height=45)

    modifcar_nombre = Button(ventana, text="MODIFICAR NOMBRE", command=modificar_ultimo_nombre, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    modifcar_nombre.place(x=55, y=70, width=230, height=45)
    
    modificar_apellido = Button(ventana, text="MODIFICAR APELLIDO", command=modificar_ultimo_apellido, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    modificar_apellido.place(x=55, y=125, width=230, height=45)
    
    modificar_correo = Button(ventana, text="MODIFICAR CORREO", command=modificar_ultimo_correo, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    modificar_correo.place(x=55, y=180, width=230, height=45)
    
    modificar_telefono = Button(ventana, text="MODIFICAR TELEFONO", command=modificar_ultimo_telefono, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    modificar_telefono.place(x=55, y=235, width=230, height=45)
    
    modificar_categoria = Button(ventana, text="MODIFICAR CATEGORIA", command=modificar_ultimo_categoria, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    modificar_categoria.place(x=55, y=290, width=230, height=45)

def comando_modificar_ultimo():
    registro = cola.mostrar_ultimo()
    if registro == None:
        return interfaz_error("❌NO HAY REGISTROS❌")
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="ULTIMO USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=25, y=15, width=290, height=45)

    usuario= Label(ventana, text=registro, font=("Segoe U", 10), bg="#ACBEF0", fg="#000000", relief="raised", border=2, justify= "left")
    usuario.place(x=35, y=70, width=270, height=215)

    modificar_boton = Button(ventana, text="MODIFICAR ULTIMO", command=modificar_ultimo_final, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    modificar_boton.place(x=55, y=295, width=230, height=45)
    
def comando_modificar():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="MODIFICAR USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=8, y=15, width=324, height=45)

    primero_boton = Button(ventana, text="MODIFICAR PRIMERO", command=comando_modificar_primero, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    primero_boton.place(x=55, y=70, width=230, height=45)

    ultimo_boton = Button(ventana, text="MODIFICAR ULTIMO", command=comando_modificar_ultimo, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
    ultimo_boton.place(x=55, y=125, width=230, height=45)

#LIMPIAR(CLEAN)
def limpiar_final():
    limpiar = cola.limpiar_cola()
    if limpiar == None:
        return interfaz_error("❌OCURRIO UN PROBLEMA❌")
    return limpiar

def comando_limpiar():
    datos_agenda = cola.mostrar_agenda()
    if datos_agenda == None:
        return interfaz_error("❌NO HAY REGISTROS❌")
    
    ventana = Toplevel()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("400x500")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="LIMPIAR AGENDA", font=("impact", 30), bg="#A1B7CF", fg="#CC0DB3", relief="groove", border=3)
    titulo.pack(pady=10)
    
    marco_principal = Frame(ventana, bg="#a3b1c6")
    marco_principal.pack(fill="both", expand=True, padx=20, pady=10)

    scrollbar = Scrollbar(marco_principal)
    scrollbar.pack(side="right", fill="y")

    canvas = Canvas(marco_principal, bg="#a3b1c6", yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=canvas.yview)

    frame_interno = Frame(canvas, bg="#a3b1c6")
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    def configurar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    
    frame_interno.bind("<Configure>", configurar_scroll)

    for texto in datos_agenda:
        marco_contacto = Frame(frame_interno, bg="#ACBEF0", relief="solid", border=1, padx=10, pady=8)
        marco_contacto.pack(fill="x", padx=10, pady=5)
        
        datos = Label(marco_contacto, text=texto, bg="#ACBEF0", font=("Arial", 10), fg="#000000", justify="left")
        datos.pack(anchor="w")

    limpiar_boton = Button(ventana, text="LIMPIAR AGENDA", command=limpiar_final, font=("impact", 16), bg="#CC0DB3", fg="#FFFFFF", relief="raised", border=5)
    limpiar_boton.pack(pady=10)

#MOSTRAR(SHOW)
def ascendente_final():
    registro = cola.mostrar_agenda()
    if registro == None:
        return interfaz_error("❌NO HAY REGISTROS❌")
    mostrar(registro, "AGENDA VIRTUAL")

def descendente_final():
    registro = cola.mostrar_ageneda_ultimo()
    if registro == None:
        return interfaz_error("❌ NO HAY REGISTROS❌")
    mostrar(registro, "AGENDA VIRTUAL")

def comando_mostrar():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x180")
    ventana.configure(bg="#a3b1c6")
    
    titulo = Label(ventana, text="MOSTRAR AGENDA", font=("impact", 30), bg="#A1B7CF", fg="#0C70AA", relief="groove", border=3)
    titulo.place(x=20, y=15, width=300, height=45)

    ascendete_boton = Button(ventana, text="⬆ASCENDENTE⬆", command=ascendente_final, font=("impact", 16), bg="#0C70AA", fg="#FFFFFF", relief="raised", border=5)
    ascendete_boton.place(x=55, y=70, width=230, height=45)

    descendente_boton = Button(ventana, text="⬇DESCENDENTE⬇", command=descendente_final, font=("impact", 16), bg="#0C70AA", fg="#FFFFFF", relief="raised", border=5)
    descendente_boton.place(x=55, y=125, width=230, height=45)

ventana = Tk()
ventana.title("AGENDA VIRTUAL")
ventana.geometry("690x460")
ventana.configure(bg="#a3b1c6")

titulo = Label(ventana, text="VENTANA PRINCIPAL", font=("impact", 60), bg="#A1B7CF", fg="#C90D55", relief="groove", border=3)
titulo.place(x=30, y=15, width=630, height=80)

agregar_boton = Button(ventana, text="AGREGAR USUARIO", command=comando_agregar, font=("impact", 16), bg="#065A06", fg="#FFFFFF", relief="raised", border=5)
agregar_boton.place(x=55, y=115, width=230, height=45)

buscar_boton = Button(ventana, text="BUSCAR USUARIO", command=comando_buscar, font=("impact", 16), bg="#0609BD", fg="#FFFFFF", relief="raised", border=5)
buscar_boton.place(x=55, y=170, width=230, height=45)

eliminar_boton = Button(ventana, text="ELIMINAR USUARIO", command=comando_eliminar, font=("impact", 16), bg="#990505", fg="#FFFFFF", relief="raised", border=5)
eliminar_boton.place(x=55, y=225, width=230, height=45)

modificar_boton = Button(ventana, text="MODIFICAR USUARIO", command=comando_modificar, font=("impact", 16), bg="#590691", fg="#FFFFFF", relief="raised", border=5)
modificar_boton.place(x=55, y=280, width=230, height=45)

limpiar_boton = Button(ventana, text="LIMPIAR AGENDA", command=comando_limpiar, font=("impact", 16), bg="#CC0DB3", fg="#FFFFFF", relief="raised", border=5)
limpiar_boton.place(x=55, y=335, width=230, height=45)

mostrar_boton = Button(ventana, text="VER AGENDA VIRTUAL", command=comando_mostrar, font=("impact", 16), bg="#0C70AA", fg="#FFFFFF", relief="raised", border=5)
mostrar_boton.place(x=55, y=390, width=230, height=45)

img_prin = Image.open("img_wanda.png")

img_prin.thumbnail((315, 335), Image.LANCZOS)

dead = ImageTk.PhotoImage(img_prin)

dead_label = Label(ventana, image=dead, relief="groove")
dead_label.place(x=320, y=117)

ventana.mainloop()
