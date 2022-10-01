from site import venv
import tkinter
from tkinter import ttk

ventana = tkinter.Tk()

ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=3)

username_label=ttk.Label(ventana,text='User Name:')
#sticky= fija el componente
#la W significa West, esta se posiciona segun las letras de la rosa de los vientos
username_label.grid(column=0,row=0,sticky=tkinter.W,padx=5,pady=5)

username_entry = ttk.Entry(ventana)
username_entry.grid(column=1,row=0,sticky=tkinter.E,padx=5,pady=5)

pass_label=ttk.Label(ventana,text='Password:')
pass_label.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5)

pass_entry = ttk.Entry(ventana,show='*')
pass_entry.grid(column=1,row=1,sticky=tkinter.E,padx=5,pady=5)

loggin_buttom = ttk.Button(ventana,text='Logging')
loggin_buttom.grid(column=1,row=2,sticky=tkinter.W,padx=5,pady=5)

ventana.mainloop()
