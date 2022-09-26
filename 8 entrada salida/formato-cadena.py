
numero=256
texto="Bytes"
flotante=1.8

# 1. forma antigua de fotmatear cadenas
print("El numero es %d, el texto es %s y el flotante es %f" % (numero,texto,flotante))

# 1.1. cuando se usa un solo valor no se necesita parentesis
#para formatear la cantidad de decimales se coloca antes de la f .numero, numero = la cantidad de decimales
print("El flotante: %.2f" % flotante)

# 2. forma antes de la ultima
print("Segunda Forma. numero: {}, texto: {}, flotante: {}".format(numero,texto,flotante))

# 3. Forma moderna
print(f'Tercera forma. numero: {numero}, texto: {texto}, float: {flotante}')