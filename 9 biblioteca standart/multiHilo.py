#programacion multihilos
import _thread
import time

def horaActual(nombre_thread, tiempo_de_espera):
    time.sleep(tiempo_de_espera)
    print(f"Hilo: {nombre_thread} - {time.ctime(time.time())}")

#de la siguiente manera se realiza la ejecucion multihilos
#(nombre de la funcion, parametros)
_thread.start_new_thread(horaActual,("thread 1",1))
_thread.start_new_thread(horaActual,("thread 2",2))

#se coloca un temporizador para dar tiempo al programa que se ejecute el multihilos
while True:
    time.sleep(0.1)