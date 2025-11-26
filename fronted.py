from tkinter import Label, Tk, Frame, Canvas, Scrollbar, Toplevel

def interfaz_encolar(registro, id):
    ventana = Tk()
    ventana.title("AGENDA VIRTUAL")
    ventana.geometry("340x350")
    ventana.configure(bg="#a3b1c6")    

    titulo = Label(ventana, text="✅REGISTRO AGREGADO✅", font=("impact", 20), bg="#ffffff", fg="#06AC00", relief="groove", border=2)
    titulo.place(x=20, y=15, width=300, height=45)

    usuario= Label(ventana, text=registro, font=("Segoe U", 10), bg="#ACBEF0", fg="#000000", relief="raised", border=2, justify= "left")
    usuario.place(x=35, y=70, width=270, height=215)

    mensaje = Label(ventana, text=f"Numero de registro: {id}", font=("impact", 16), bg="#ffffff", fg="#000000", relief="raised", border=5)
    mensaje.place(x=45, y=295, width=250, height=45)
