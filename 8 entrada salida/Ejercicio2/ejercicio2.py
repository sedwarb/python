import pickle

guardar=False

class Vehiculo:
    puertas=None
    tipo=None #Coupe, Sedan, entre otros
    motor=None #1000 cc, 1200 cc, entre otros
    neumatico=None #R13, R14, R15, entre otros

    def __init__(self,datos_vehiculo):
        self.puertas=datos_vehiculo["puertas"]
        self.tipo=datos_vehiculo["tipo"]
        self.motor=datos_vehiculo["motor"]
        self.neumatico=datos_vehiculo["neumatico"]
    
    def datos(self):
        print("Datos del vehiculo")
        print("Cantidad de Puertas: ", self.puertas)
        print("Tipo de Vehiculo: ", self.tipo.capitalize())
        print("Cilindraje del Motor: ", self.motor, "cc")
        print("Tamano del Rin: ", self.neumatico.capitalize())

kwid = Vehiculo({"puertas":5,"tipo":"coupe","motor":0.98,"neumatico":"r14"})

if guardar:
    f = open('vehiculo.bin','wb')
    print("Se ha almacenado la clase")
    pickle.dump(kwid,f)
    f.close()
else:
    f = open('vehiculo.bin','rb')
    renault_kwid = pickle.load(f)
    renault_kwid.datos()
    f.close()