opcion = 3

#escritura y elimina lo existente
if opcion==1:
    f = open('./prueba-escritura.txt','w')
    f.write("Linea1\n")
    f.write("Linea2\n")
    f.close()

#escribe al final del fichero
if opcion==2:
    f = open('./prueba-escritura.txt','a')
    f.write("Linea3\n")
    f.write("Linea4\n")
    f.close()

#escribe varias lineas
if opcion==3:
    f = open('./prueba-escritura.txt','w')
    lista=['lineaArray1\n','lineaArray2\n','lineaArray3\n']
    f.writelines(lista)
    f.close()