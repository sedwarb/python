import tkinter
from tkinter import StringVar, Tk, ttk

ventana = tkinter.Tk()

languages = ["Python","Perl","Java","C++","C"]
items = StringVar(value=languages)

label1=tkinter.Label(ventana,text='Lenguajes de Programacion', bg='yellow', fg='blue')
label1.grid(column=0,row=0,sticky=tkinter.W)

lista=tkinter.Listbox(ventana,height=15,listvariable=items)
lista.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5)

ventana.mainloop()