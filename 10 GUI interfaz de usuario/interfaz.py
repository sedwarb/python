import tkinter

#instancias la clase en la variable
ventana = tkinter.Tk()

#instancio el componente que voy a mostrar, en este caso un label, los parametros son, la instancia
#de tk y el texto que va a mostrar. bg=color de fondo fg=color de letra
label_saludo=tkinter.Label(ventana,text='Hola Python', bg='yellow', fg='blue')

#usa la geometria pack para mostrar el componente (hay diferentes tipos de geometrias, que es la forma...
#en que se organizan los componentes en una ventana
# ipadx= ancho e ipady= alto fill=rellena si es x,y o both
label_saludo.pack(ipadx=50,ipady=50, fill='x')

label_adios=tkinter.Label(ventana,text='Adios Python', bg='black', fg='white')
label_adios.pack(ipadx=50,ipady=100, fill='y')

#expand mantiene el componente centrado
label_otro=tkinter.Label(ventana,text='Otro Python', bg='blue', fg='white')
label_otro.pack(ipadx=50,ipady=100, expand=True)

#side= ubicacion del componente
label_L=tkinter.Label(ventana,text='Left', bg='blue', fg='white')
label_L.pack(ipadx=50,ipady=100, side='left')

label_R=tkinter.Label(ventana,text='Right', bg='red', fg='white')
label_R.pack(ipadx=50,ipady=100, side='right')


#muestras la ventana
ventana.mainloop()