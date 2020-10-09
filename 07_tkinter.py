from tkinter import Tk, Label

window = Tk()
window.title = 'Aplicación Gráfica!'

label = Label(text='Texto informativo', font=('Arial', 80), fg='red', bg='blue')
label.pack()

window.mainloop()
