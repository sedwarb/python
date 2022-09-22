import suma as s
#import operaciones.resta as r
#Otra manera de importar...
from operaciones import resta as r
import otras.globals as glob
#Se importa con el nombre del modulo as -->> el nombre con que lo 
#Para importar modulos dentro de paquetes se hace como arriba operaciones.resta

def main():
    nsuma = s.Suma()
    print(s.suma(4,4))
    print("uso de la class Suma con negativo: ", nsuma.otrasuma(4,4))
    print("Resta: ", r.resta(5,5))
    #Uso __name__ para que me muestre el nombre del fichero actual
    print(__name__)
    #glob.modGlo()

if __name__ == '__main__':
    main()