f = open('ejercicio1.txt','a')
lineas=["PASOS PARA REALIZAR EL EJERCICIO 1 MODULO 8\n",
"1. Crear Archivo y Abrirlo\n","2. Escribir dentro del Archivo\n",
"3. Acceder dos veces al Archivo Creado\n"]
f.writelines(lineas)
f.close()

f = open('./ejercicio1.txt','r')
f.read()
f.close()