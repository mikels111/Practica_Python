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
ventana.geometry("150x160")

class formulario(self):

    numero1 = StringVar()
    numero2 = StringVar()
    resultado = StringVar()
    
    def suma(self):
        #resultado.set(numero1.get() + numero2.get())
        try:
            MessageBox.showinfo("Resultado", float(numero1.get()) + float(numero2.get()))
            numero1.set("")
        except:
            MessageBox.showerror("Resultado", "Ha ocurrido un error")
        

    def resta(self):
        #    resultado.set(numero1.get() - numero2.get())
        try:
            MessageBox.showinfo("Resultado", float(numero1.get()) - float(numero2.get()))
            numero1.set("")
        except:
            MessageBox.showerror("Resultado", "Ha ocurrido un error")

    def multi(self):
        #    resultado.set(numero1.get() * numero2.get())
        try:
            MessageBox.showinfo("Resultado", float(numero1.get()) * float(numero2.get()))
            numero1.set("")
        except:
            MessageBox.showerror("Resultado", "Ha ocurrido un error")
            
    def division(self):
        #    resultado.set(numero1.get() / numero2.get())
        try:
            MessageBox.showinfo("Resultado", float(numero1.get()) / float(numero2.get()))
            numero1.set("")
        except:
            MessageBox.showerror("Resultado", "Ha ocurrido un error")

            
label = Label(ventana,text="")
label.grid(columnspan=2)
label.config(padx=5)


# Entradas de texto
entry_1 = Entry(ventana, textvariable=numero1).grid(column=2, pady=4)
entry_2 = Entry(ventana, textvariable=numero2).grid(column=2, pady=4)

# Marco
marco = Frame(ventana, width=120, height=100)
marco.config(bd=3, relief=SOLID)
marco.grid(column=2)
#marco.pack_propagate(False)para que no se deforme el marco

# Botones
boton_suma = Button(marco, text="+", command=suma).grid(padx=5, pady=5, column=1, row=1)
boton_resta = Button(marco, text="-", command=resta).grid(padx=5, pady=5, column=2, row=1)
boton_multi = Button(marco, text="x", command=multi).grid(padx=5, pady=5, column=1, row=2)
boton_divi = Button(marco, text="/", command=division).grid(padx=5, pady=5, column=2, row=2)

# Label resultado
#Label(ventana, textvariable=resultado).grid(column=2)

ventana.mainloop()
