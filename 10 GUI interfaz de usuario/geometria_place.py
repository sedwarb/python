import sys
import tkinter
from tkinter import ttk

ventana = tkinter.Tk()

label1=tkinter.Label(ventana,text='Posicionamiento absoluto', bg='yellow', fg='blue')
label1.place(x=10,y=50)

label2=tkinter.Label(ventana,text='Otro Label', bg='blue', fg='yellow')
#posicionamiento relativo
label2.place(relx=0.10,rely=0.15,relwidth=0.5,anchor='nw')

#lo siguiente se usa para finalizar el programa donde este se encuentre
#sys.exit(0)

ventana.mainloop()

