import logging
con = False
#ficheros de registro
if con == True:
    #Al colocar la siguiente configuracion muestra info
    logging.basicConfig(level=logging.INFO)

#en este caso no muestra nada en consola
logging.info("Arrancando programa")

#en este si muestra en consola
logging.warning("Hace Calor")

#para ver mas de este modulo, investigar en la biblioteca de python