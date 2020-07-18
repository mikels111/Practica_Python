from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("500x600")
Label(ventana, text="hola mundo").pack(anchor=W)
imagen = Image.open("./21.tkinter/imagenes/the wall.jpg")
render = ImageTk.PhotoImage(imagen)
cuadro = Label(ventana, image=render)
cuadro.config(height=500,width=500)
cuadro.pack()
ventana.mainloop()
