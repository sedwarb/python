#permisos de archivos r: lectura, a: se escribe al final, 
# w: escritura, voy sustituir por nueva escritura, x: create

#Se abre el fichero en la direccio indicada y en la condicion indicada
f = open('./modulo8.txt','r')

opcion = 3

if opcion==1:
    #para leer linea a linea un fichero
    #la funcion readline lee la linea actual y se posiciona en la siguiente
    ndatos="a"
    while ndatos != "":
        ndatos = f.readline()
        print(ndatos)

if opcion==2:
    #asignas el contenido en una variable, si en el read(9) coloco un numero
    #es el numero de bytes que voy a leer, un byte es un caracter, incluyendo \n que es un caracter
    datos = f.read()
    # \n es el salto de linea
    print(datos.split('\n'))

if opcion==3:
    #para que cada linea se convierta en una posicion de un array
    datos=f.readlines()
    print(datos)

#cierras el fichero
f.close()