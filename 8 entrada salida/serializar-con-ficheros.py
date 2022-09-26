import pickle

op = 2

#escribe un objeto en un fichero

class Juguete:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def getnombre(self):
        return self.nombre

j1 = Juguete("Thor",100.7)

#escribir  
if op == 1:
    f = open('./serializar.bin','wb')
    pickle.dump(j1,f)
    f.close()

#leer
if op == 2:
    f = open('./serializar.bin','rb')
    thor = pickle.load(f)
    print(thor.getnombre(), "Cuesta:", thor.precio)
    f.close()