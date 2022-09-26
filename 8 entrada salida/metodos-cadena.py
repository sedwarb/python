cadena = "en un lugar muy muy lejano"

#capitalize coloca la primera letra en mayuscula y las otras en minuscula
print(cadena.capitalize())
#title coloca la primera letra de cada palabra en mayuscula
print(cadena.title())
#count cuantas veces aparece una letra en una cadena
print(cadena.count('u'))
#lower para colocar todo en minuscula y upper en mayuscula
print(cadena.lower())
print(cadena.upper())
#para saber si una cadena es un numero
numero = "3"
print(numero.isdigit())
#para saber si una cadena es una letra
print(numero.isalpha())
#para saber si una cadena es una letra o numero
otro="%"
print(otro.isalnum())
#eliminar espacios en las cadenas
cadena2 = "   tres espacios antes y despues   "
print(cadena2)
print(cadena2.strip())
#lstrip quita los espacion de la izquierda y rstrip los de la derecha

#para convertir una cadena en un array, entre los parentesis puede colocar por 
#que condicion se va a dividir, si el texto tuviese coma, lo puede dividir por coma
#","
print(cadena.split())

#para saber si una cadena comienza con algo en especifico
print(cadena.startswith("en"))
#para como finaliza endswith