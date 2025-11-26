from clase import Sistema
from tkinter import Button, Entry, Label, Tk, Frame, Canvas, Scrollbar, Toplevel
from cola import Cola
from fronted import interfaz_encolar, mostrar, interfaz_buscar_primero, interfaz_buscar_ultimo
import random
cola = Cola()


#AGREGAR(SAVE)
def agregar_final(codigo, nombre, apellido, correo, telefono, categoria, ventana):
    if codigo == "" or nombre == "" or apellido == "" or correo == "" or telefono == "" or categoria == "":
        return None
    registro = Sistema(int(codigo), nombre, apellido, correo, int(telefono), categoria)
    usuario = cola.encolar(registro)
    if usuario == None:
        return None
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
    "TRABAJO",
    "EMERGENCIA",
    "VECINO",
    "ESTUDIO",
    "CLIENTE",
    "PROVEEDOR",
    "SERVICIO",
    "OTRO"
    ]
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("430x430")
    ventana.configure(bg="#a3b1c6")
    titulo = Label(ventana, text="👤REGISTRAR USUARIO👤", font=("impact", 20), bg="#137bc0", fg="#FF0000", relief="groove", border=2)
    titulo.place(x=45, y=15, width=350, height=45)

    label_codigo = Label(ventana, text="✅CODIGO:", font=("impact", 16), bg="#FFFFFF", fg="#000000", relief="raised", border=5)
    label_codigo.place(x=15, y=70, width=140, height=40)
    entry_codigo = Entry(ventana,  font=("times", 14, "bold"), relief="solid", border=2)
    entry_codigo.place(x=170, y=70, width=250, height=40)

    label_nombre= Label(ventana, text="✅NOMBRES:", font=("impact", 16), bg="#FFFFFF", fg="#000000", relief="raised", border=5)
    label_nombre.place(x=15, y=120, width=140, height=40)
    entry_nombre = Entry(ventana, font=("times", 14, "bold"), relief="solid", border=2)
    entry_nombre.place(x=170, y=120, width=250, height=40)
    entry_nombre.insert(0, random.choice(dic_nombres))

    label_apellido= Label(ventana, text="✅APELLIDOS:", font=("impact", 16), bg="#FFFFFF", fg="#000000", relief="raised", border=5)
    label_apellido.place(x=15, y=170, width=140, height=40)
    entry_apellido = Entry(ventana, font=("times", 14, "bold"), relief="solid", border=2)
    entry_apellido.place(x=170, y=170, width=250, height=40)
    entry_apellido.insert(0, random.choice(dic_apellidos))

    label_correo= Label(ventana, text="✅CORREO:", font=("impact", 16), bg="#FFFFFF", fg="#000000", relief="raised", border=5)
    label_correo.place(x=15, y=220, width=140, height=40)
    entry_correo = Entry(ventana, font=("times", 14, "bold"), relief="solid", border=2)
    entry_correo.place(x=170, y=220, width=250, height=40)
    entry_correo.insert(0, random.choice(dic_correo))

    label_telefono= Label(ventana, text="✅TELOFONO:", font=("impact", 16), bg="#FFFFFF", fg="#000000", relief="raised", border=5)
    label_telefono.place(x=15, y=270, width=140, height=40)
    entry_telefono = Entry(ventana, font=("times", 14, "bold"), relief="solid", border=2)
    entry_telefono.place(x=170, y=270, width=250, height=40)
    entry_telefono.insert(0, random.choice(dic_telefono))

    label_categoria= Label(ventana, text="✅CATEGORIA:", font=("impact", 16), bg="#FFFFFF", fg="#000000", relief="raised", border=5)
    label_categoria.place(x=15, y=320, width=140, height=40)
    entry_categoria = Entry(ventana, font=("times", 14, "bold"), relief="solid", border=2)
    entry_categoria.place(x=170, y=320, width=250, height=40)
    entry_categoria.insert(0, random.choice(dic_categoria))

    agregar = Button(ventana, text="AGREGAR USUARIO ✅", command=lambda: (agregar_final(entry_codigo.get(), entry_nombre.get(), entry_apellido.get(), entry_correo.get(), entry_telefono.get(), entry_categoria.get(), ventana)), bg="#137bc0", fg="#FF0000", font=("impact", 17), width=25, relief="groove", border=2)
    agregar.place(x=100, y=370, width=230, height=45)

#BUSCAR(SEARCH)
def comando_buscar_ultimo():
    usuario = cola.mostrar_ultimo()
    if usuario == None:
        return None
    return interfaz_buscar_ultimo(usuario)

def comando_buscar_primero():
    usuario = cola.mostrar_frente()
    if usuario == None:
        return None
    return interfaz_buscar_primero(usuario)

def comando_buscar():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x240")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="🔍BUSCAR USUARIO🔎", font=("impact", 20), bg="#ffffff", fg="#0165FA", relief="groove", border=2)
    titulo.place(x=20, y=15, width=300, height=45)

    primero_boton = Button(ventana, text="🔍BUSCAR PRIMERO🔎", command=comando_buscar_primero, font=("impact", 16), bg="#FFFFFF", fg="#FF0000", relief="raised", border=5)
    primero_boton.place(x=55, y=70, width=230, height=45)

    ultimo_boton = Button(ventana, text="🔍BUSCAR ULTIMO🔎", command=comando_buscar_ultimo, font=("impact", 16), bg="#FFFFFF", fg="#FF0000", relief="raised", border=5)
    ultimo_boton.place(x=55, y=125, width=230, height=45)
    
    especifico_boton = Button(ventana, text="🔍BUSCAR ESPECIFICO🔎", command=comando_agregar, font=("impact", 16), bg="#FFFFFF", fg="#FF0000", relief="raised", border=5)
    especifico_boton.place(x=55, y=180, width=230, height=45)

#ELIMINAR(DELETE)
def eliminar_primero_final():
    usuario = cola.desencolar_primero()
    if usuario == None:
        return None
    return usuario

def comando_eliminar_primero():
    usuario = cola.mostrar_frente()
    if usuario == None:
        return None
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="⚠️PRIMER USUARIO⚠️", font=("impact", 20), bg="#ffffff", fg="#FF0000", relief="groove", border=2)
    titulo.place(x=20, y=15, width=300, height=45)

    usuario= Label(ventana, text=usuario, font=("Segoe U", 10), bg="#ACBEF0", fg="#000000", relief="raised", border=2, justify= "left")
    usuario.place(x=35, y=70, width=270, height=215)

    eliminar = Button(ventana, text="❌ELIMINAR PRIMERO❌", command=eliminar_primero_final, font=("impact", 16), bg="#137bc0", fg="#FF0000", relief="raised", border=5)
    eliminar.place(x=55, y=295, width=220, height=45)

def eliminar_ultimo_final():
    usuario = cola.desencolar_ultimo()
    if usuario == None:
        return None
    return usuario

def comando_eliminar_ultimo():
    usuario = cola.mostrar_ultimo()
    if usuario == None:
        return None
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="⚠️ULTIMO USUARIO⚠️", font=("impact", 20), bg="#ffffff", fg="#FF0000", relief="groove", border=2)
    titulo.place(x=20, y=15, width=300, height=45)

    usuario= Label(ventana, text=usuario, font=("Segoe U", 10), bg="#ACBEF0", fg="#000000", relief="raised", border=2, justify= "left")
    usuario.place(x=35, y=70, width=270, height=215)

    eliminar = Button(ventana, text="❌ELIMINAR PRIMERO❌", command=eliminar_ultimo_final, font=("impact", 16), bg="#137bc0", fg="#FF0000", relief="raised", border=5)
    eliminar.place(x=55, y=295, width=220, height=45)

def comando_eliminar():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x240")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="⚠️ELIMINAR USUARIO⚠️", font=("impact", 20), bg="#137bc0", fg="#FF0000", relief="groove", border=2)
    titulo.place(x=20, y=15, width=300, height=45)

    primero_boton = Button(ventana, text="❌ELIMINAR PRIMERO❌", command=comando_eliminar_primero, font=("impact", 16), bg="#FFFFFF", fg="#FF0000", relief="raised", border=5)
    primero_boton.place(x=55, y=70, width=230, height=45)

    ultimo_boton = Button(ventana, text="❌ELIMINAR ULTIMO❌", command=comando_eliminar_ultimo, font=("impact", 16), bg="#FFFFFF", fg="#FF0000", relief="raised", border=5)
    ultimo_boton.place(x=55, y=125, width=230, height=45)
    
    especifico_boton = Button(ventana, text="❌ELIMINAR ESPECIFICO❌", command=comando_agregar, font=("impact", 16), bg="#FFFFFF", fg="#FF0000", relief="raised", border=5)
    especifico_boton.place(x=55, y=180, width=230, height=45)

#MODIFICAR(UPDATE)



#LIMPIAR(CLEAN)
def limpiar_final():
    limpiar = cola.limpiar_cola()
    if limpiar == None:
        return None
    return limpiar

def comando_limpiar():
    datos_agenda = cola.mostrar_agenda_frente()
    if datos_agenda == None:
        return None
    
    ventana = Toplevel()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("400x500")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="🚫 LIMPIAR AGENDA 🚫", font=("impact", 20), bg="#137bc0", fg="#E91313", relief="groove", border=2)
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

    limpiar_boton = Button(ventana, text="🚫 LIMPIAR AGENDA 🚫", command=limpiar_final, font=("impact", 16), bg="#137bc0", fg="#FF0000", relief="raised", border=5)
    limpiar_boton.pack(pady=10)

#MOSTRAR(SHOW)
def ascendente_final():
    registro = cola.mostrar_agenda_frente()
    if registro == None:
        return None
    mostrar(registro)

def descendente_final():
    registro = cola.mostrar_ageneda_ultimo()
    if registro == None:
        return None
    mostrar(registro)

def comando_mostrar():
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x410")
    ventana.configure(bg="#a3b1c6")
    
    titulo = Label(ventana, text="📁MOSTRAR AGENDA📁", font=("impact", 20), bg="#137bc0", fg="#E91313", relief="groove", border=2)
    titulo.place(x=20, y=15, width=300, height=45)

    ascendete_boton = Button(ventana, text="⬆ASCENDENTE⬆", command=ascendente_final, font=("impact", 16), bg="#FFFFFF", fg="#FF0000", relief="raised", border=5)
    ascendete_boton.place(x=55, y=70, width=230, height=45)

    descendente_boton = Button(ventana, text="⬇DESCENDENTE⬇", command=descendente_final, font=("impact", 16), bg="#FFFFFF", fg="#FF0000", relief="raised", border=5)
    descendente_boton.place(x=55, y=125, width=230, height=45)

ventana = Tk()
ventana.title("AGENDA VIRTUAL")
ventana.geometry("340x410")
ventana.configure(bg="#a3b1c6")

titulo = Label(ventana, text="👤VENTANA PRINCIPAL👤", font=("impact", 20), bg="#FFFFFF", fg="#9700FC", relief="groove", border=2)
titulo.place(x=20, y=15, width=300, height=45)

agregar_boton = Button(ventana, text="AGREGAR USUARIO✅", command=comando_agregar, font=("impact", 16), bg="#FFFFFF", fg="#000000", relief="raised", border=5)
agregar_boton.place(x=55, y=70, width=230, height=45)

buscar_boton = Button(ventana, text="BUSCAR USUARIO🔎", command=comando_buscar, font=("impact", 16), bg="#FFFFFF", fg="#000000", relief="raised", border=5)
buscar_boton.place(x=55, y=125, width=230, height=45)

eliminar_boton = Button(ventana, text="ELIMINAR USUARIO⛔", command=comando_eliminar, font=("impact", 16), bg="#FFFFFF", fg="#000000", relief="raised", border=5)
eliminar_boton.place(x=55, y=180, width=230, height=45)

modificar_boton = Button(ventana, text="MODIFICAR USUARIO🔓", command=comando_agregar, font=("impact", 16), bg="#FFFFFF", fg="#000000", relief="raised", border=5)
modificar_boton.place(x=55, y=235, width=230, height=45)

limpiar_boton = Button(ventana, text="LIMPIAR AGENDA🗑️", command=comando_limpiar, font=("impact", 16), bg="#FFFFFF", fg="#000000", relief="raised", border=5)
limpiar_boton.place(x=55, y=290, width=230, height=45)

mostrar_boton = Button(ventana, text="VER AGENDA VIRTUAL📦", command=comando_mostrar, font=("impact", 16), bg="#FFFFFF", fg="#000000", relief="raised", border=5)
mostrar_boton.place(x=55, y=345, width=230, height=45)

ventana.mainloop()
