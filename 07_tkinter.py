from tkinter import *
from tkinter.ttk import Combobox


class App:
    def __init__(self):
        self.__contador = 0
        self.window = Tk()
        self.window.title = 'Aplicación Gráfica!'
        # window.maxsize(width=300, height=200)
        # window.minsize(width=100, height=120)
        # window.geometry('800x400')

        Label(text='Hola!', font=('Arial Bold', 36)).grid(column=0, row=0)
        self.text = Label(text='Esto sale más pequeño', font=('Arial', 24))
        self.text.grid(column=1, row=0)

        Button(text='Pulsa', command=lambda: self.button()).grid(column=1, row=1)

        self.entry = Entry()
        self.entry.grid(column=0, row=2)
        Button(text='Pulsa').grid(column=1, row=2)

        self.combo = Combobox(values=['Cero', 'Uno', 'Dos', 'Tres', 'Cuatro'], state='readonly')
        self.combo.grid(column=0, row=3)
        self.combo.current(0)
        Button(text='Pulsa').grid(column=1, row=3)

        self.window.mainloop()

    def button(self):
        self.__contador += 1

if __name__ == '__main__':
    App()