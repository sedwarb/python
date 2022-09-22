import pprint

def chage():
    globals()['variable'] = 20

def pruebaLocal():
    valor1 = 30
    otro=60
    pprint.pprint(locals())
    

class Saluda:
    cantidad=1
    def saludo(Self):
        print("Hola")
    def mosCantidad(Self):
        print(Self.cantidad)

variable = 5
print(variable)
chage()
pprint.pprint(globals())
# A continuacion uso globals para modificar la variable
print("variable modificada por globals: ", variable)

#Puedo usar globals para acceder al metodo de una clase
p = Saluda()
globals()['p'].saludo()
globals()['p'].mosCantidad()

print("muestra locals de una funcion")
pruebaLocal()
