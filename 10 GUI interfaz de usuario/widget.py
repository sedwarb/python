from tabnanny import check
import tkinter
from tkinter import StringVar, Tk, ttk

ventana = tkinter.Tk()
sistemas_op=['windows','macos','linux','android','freedos']
items = StringVar(value=sistemas_op)

frame=ttk.Frame(ventana)
frame.grid(column=0,row=0,sticky=tkinter.W)
frame.config(width=800,height=600)
frame.config(relief="sunken")

label1=tkinter.Label(frame,text='Label', bg='yellow', fg='blue')
label1.grid(column=0,row=0,sticky=tkinter.W,padx=50,pady=50)

lista=tkinter.Listbox(frame,height=15,listvariable=items)
lista.grid(column=0,row=1,sticky=tkinter.W,padx=50,pady=50)

seleccion=tkinter.StringVar()
acepto=tkinter.StringVar()

r1 = tkinter.Radiobutton(frame,text='Si',value='SI',variable=seleccion)
r2 = tkinter.Radiobutton(frame,text='No',value='NO',variable=seleccion)
r1.grid(column=0,row=2,sticky=tkinter.W,padx=5,pady=5)
r2.grid(column=0,row=3,sticky=tkinter.W,padx=5,pady=5)

def funcion(event):
    print('cualquier cosa')

def salir(event):
    ventana.quit()

ch=tkinter.Checkbutton(frame,text='Aceptar',variable=acepto,command=funcion)
ch.grid(column=0,row=4,sticky=tkinter.W,padx=5,pady=5)

btn = tkinter.Button(frame,text='Haz Click')
btn.grid(column=0,row=5,sticky=tkinter.E,padx=5,pady=5)
btn.bind('<Button-1>',funcion)

btn = tkinter.Button(frame,text='Salir')
btn.grid(column=0,row=6,sticky=tkinter.E,padx=5,pady=5)
btn.bind('<Button-1>',salir)


ventana.mainloop()