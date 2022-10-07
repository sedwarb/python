import tkinter
from tkinter import ttk
import random

colors=['yellow','blue','green','white','black','orange']
ventana = tkinter.Tk()

for x in range(0,10):
    color=random.randint(0,len(colors)-1)
    color2=random.randint(0,len(colors)-1)
    label1=tkinter.Label(ventana,text='Etiqueta', bg=colors[color], fg=colors[color2])
    label1.place(x=random.randint(0,100),y=random.randint(0,100))

ventana.mainloop()