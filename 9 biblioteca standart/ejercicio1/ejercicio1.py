cadena = input("Introduce los paises separados por coma: ")
ncadena = ""
inicio = True
for i in sorted(set(cadena.split(","))):
    if inicio:
        ncadena=i
        inicio=False
        continue
    ncadena=ncadena+","+i

print(ncadena)