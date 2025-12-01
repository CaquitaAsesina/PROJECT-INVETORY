from tkinter import Label, Tk, Frame, Canvas, Scrollbar, Toplevel
from PIL import Image, ImageTk
#AGREGAR(SAVE)
def interfaz_encolar(registro, id):
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")    

    titulo = Label(ventana, text="REGIS. AGREGADO", font=("impact", 30), bg="#A1B7CF", fg="#065A06", relief="groove", border=3)
    titulo.place(x=20, y=15, width=300, height=45)

    usuario= Label(ventana, text=registro, font=("Segoe U", 10), bg="#ACBEF0", fg="#000000", relief="raised", border=2, justify= "left")
    usuario.place(x=35, y=70, width=270, height=215)

    mensaje = Label(ventana, text=f"Numero de registro: {id}", font=("impact", 16), bg="#9CC4A6", fg="#000000", relief="raised", border=5)
    mensaje.place(x=45, y=295, width=250, height=45)

    ventana.after(1000, ventana.destroy)

#MOSTRAR(SHOW)
def mostrar(datos_agenda, titulo):
    ventana = Toplevel()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("400x500")
    ventana.configure(bg="#a3b1c6")
    titulo = Label(ventana, text=titulo, font=("impact", 20), bg="#A1B7CF", fg="#0C70AA", relief="groove", border=3)
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

#BUSCAR(SEARCH)
def interfaz_buscar_primero(usuario):
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="PRIMER USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#0609BD", relief="groove", border=3)
    titulo.place(x=20, y=15, width=300, height=45)

    usuario= Label(ventana, text=usuario, font=("Segoe U", 10), bg="#ACBEF0", fg="#000000", relief="raised", border=2, justify= "left")
    usuario.place(x=35, y=70, width=270, height=215)

    mensaje = Label(ventana, text="USUARIO ENCONTRADO", font=("impact", 16), bg="#8D8ED3", fg="#000000", relief="raised", border=5)
    mensaje.place(x=45, y=295, width=250, height=45)

def interfaz_buscar_ultimo(usuario):
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="ULTIMO USUARIO", font=("impact", 30), bg="#A1B7CF", fg="#0609BD", relief="groove", border=3)
    titulo.place(x=20, y=15, width=300, height=45)

    usuario= Label(ventana, text=usuario, font=("Segoe U", 10), bg="#ACBEF0", fg="#000000", relief="raised", border=2, justify= "left")
    usuario.place(x=35, y=70, width=270, height=215)

    mensaje = Label(ventana, text="USUARIO ENCONTRADO", font=("impact", 16), bg="#8D8ED3", fg="#000000", relief="raised", border=5)
    mensaje.place(x=45, y=295, width=250, height=45)

def interfaz_buscar_especifico(usuario, titulo):
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text=titulo, font=("impact", 30), bg="#A1B7CF", fg="#0609BD", relief="groove", border=3)
    titulo.place(x=20, y=15, width=300, height=45)

    usuario= Label(ventana, text=usuario, font=("Segoe U", 10), bg="#ACBEF0", fg="#000000", relief="raised", border=2, justify= "left")
    usuario.place(x=35, y=70, width=270, height=215)

    mensaje = Label(ventana, text="USUARIO ENCONTRADO", font=("impact", 16), bg="#8D8ED3", fg="#000000", relief="raised", border=5)
    mensaje.place(x=45, y=295, width=250, height=45)


#ELIMINAR(DELETE)
def interfaz_eliminar_especifico(usuario, titulo):
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text=titulo, font=("impact", 30), bg="#A1B7CF", fg="#990505", relief="groove", border=2)
    titulo.place(x=20, y=15, width=300, height=45)

    usuario= Label(ventana, text=usuario, font=("Segoe U", 10), bg="#ACBEF0", fg="#000000", relief="raised", border=2, justify= "left")
    usuario.place(x=35, y=70, width=270, height=215)

    mensaje = Label(ventana, text="USUARIO ELIMINADO", font=("impact", 16), bg="#D47878", fg="#000000", relief="raised", border=5)
    mensaje.place(x=45, y=295, width=250, height=45)

def interfaz_error(message):
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x130")
    ventana.configure(bg="#a3b1c6")

    titulo = Label(ventana, text="PROBLEMA DETECTADO", font=("impact", 20), bg="#3fc4f8", fg="#F30000", relief="groove", border=3)
    titulo.place(x=11, y=15, width=320, height=45)

    usuario= Label(ventana, text=message, font=("Segoe U", 12), bg="#ACBEF0", fg="#FF0000", relief="groove", border=2)
    usuario.place(x=35, y=70, width=270, height=50)

    ventana.after(1000, ventana.destroy)

#MODIFICA (UPDATE)
def interfaz_modificar(registro, modificado):
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")    

    titulo = Label(ventana, text="USUARIO MODIFICADO", font=("impact", 20), bg="#A1B7CF", fg="#590691", relief="groove", border=3)
    titulo.place(x=11, y=15, width=320, height=45)

    usuario= Label(ventana, text=registro, font=("Segoe U", 10), bg="#BA8FD6", fg="#000000", relief="raised", border=2, justify= "left")
    usuario.place(x=35, y=70, width=270, height=215)

    mensaje = Label(ventana, text=modificado, font=("impact", 16), bg="#590691", fg="#000000", relief="raised", border=5)
    mensaje.place(x=45, y=295, width=250, height=45)

    
    