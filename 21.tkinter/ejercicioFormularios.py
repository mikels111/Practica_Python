"""
Calculadora

- Dos campos de texto
- 4 botones para las operaciones
- Mostrar el resultado en una alerta
"""
from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("200x200")

class Formulario:

    def __init__(self):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()    

    def comprobar(self, numero):
        try:
            result = float(numero)
        except:
            result = 0
            MessageBox.showerror("Resultado", "Ha ocurrido un error")
        
        return result

    def suma(self):
        self.resultado = self.comprobar(self.numero1.get()) + self.comprobar((self.numero2.get()))
        self.numero1.set("")
        self.numero2.set("")
        self.mostrarResultado()
        
        
    def resta(self):
        self.resultado = self.comprobar(self.numero1.get()) - self.comprobar((self.numero2.get()))
        self.numero1.set("")
        self.numero2.set("")
        self.mostrarResultado()

    def multi(self):
        self.resultado = "Resultado", self.comprobar(self.numero1.get()) * self.comprobar((self.numero2.get()))
        self.numero1.set("")
        self.numero2.set("")
        self.mostrarResultado()

    def division(self):
        self.resultado = self.comprobar(self.numero1.get()) / self.comprobar(self.numero2.get())
        self.numero1.set("")
        self.numero2.set("")
        self.mostrarResultado()

    def mostrarResultado(self):
        MessageBox.showinfo("Resultado", self.resultado) 

formulario1 = Formulario()

# Entradas de texto
entry_1 = Entry(ventana, textvariable=formulario1.numero1).grid(column=2, pady=4)
entry_2 = Entry(ventana, textvariable=formulario1.numero2).grid(column=2, pady=4)  

label = Label(ventana,text="")
label.grid(columnspan=2)
label.config(padx=5)

# Marco
marco = Frame(ventana, width=120, height=100)
marco.config(bd=3, relief=SOLID)
marco.grid(column=2)
#marco.pack_propagate(False)para que no se deforme el marco

# Botones
boton_suma = Button(marco, text="+", command=formulario1.suma).grid(padx=5, pady=5, column=1, row=1)
boton_resta = Button(marco, text="-", command=formulario1.resta).grid(padx=5, pady=5, column=2, row=1)
boton_multi = Button(marco, text="x", command=formulario1.multi).grid(padx=5, pady=5, column=1, row=2)
boton_divi = Button(marco, text="/", command=formulario1.division).grid(padx=5, pady=5, column=2, row=2)

# Label resultado
#Label(ventana, textvariable=resultado).grid(column=2)

ventana.mainloop()
