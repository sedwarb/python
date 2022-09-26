num=511
print(type(num))

numtxt = str(num)
print(type(numtxt))

print(repr(num))
print(numtxt)

class Juguete:
    nombre=""
    precio=0.0

    def __init__(Self,nombre,precio):
        Self.nombre=nombre
        Self.precio=precio
    
    def __str__(Self):
        return f'El Juguete {Self.nombre} cuesta {Self.precio}'

    def __repr__(self):
        return f'Juguete({self.nombre},{self.precio})'

j1 = Juguete("Masinger Z",100.5)

#lo convierte a cadena, por el uso de __str__ en la clase
print(type(str(j1)))

#para una salida de produccion se usa el str, el print ya tiene el str implicito
print(j1)

#representacion formal
print(type(j1))

#para una salida de depuracion se usa repr
print(repr(j1))