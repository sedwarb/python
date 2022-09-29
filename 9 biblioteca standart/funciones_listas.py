from functools import reduce

numeros = [13,2,3,4,5,6,7,8,9,10]

opcion="otras"

if opcion == "filter":    
    #funcion filter
    def pares(x):
        if x%2 == 0:
            return True
        else:
            return False

    print(list(filter(pares,numeros)))
    #impares
    print(list(filter(lambda x: x%2 != 0,numeros)))

    print(list(filter(lambda x: str(x).startswith("ga"),["gato","abuela","gafo"])))

if opcion == "map":
    #funcion map
    print(list(map(lambda x: x*x,[1,2,3,4,8])))

if opcion == "reduce":
    #funcion reduce, se debe importar: from functools import reduce
    print(reduce(lambda a,b: a+b,[1,2,3,4,8]))

if opcion == "zip":
    #funcion zip
    #une el contenido de dos objetos iterables
    cursos = ["java","python","c"]
    asistentes = [20,50,10]
    print(list(zip(cursos,asistentes)))

if opcion == "all":
    #any y all
    #any verifica que aunque sea una se cumpla, all todas se cumplan
    val = [1==1,2==2,3==4]
    print("Any:", any(val))
    print("All:", all(val))

if opcion == "round":
    print(list(map(lambda x: round(x),[5.1,5.6,5.3])))

if opcion == "otras":
    print("Minimo: ", min(numeros))
    print("Elevados al cuadrado:", list(map(lambda x: pow(2,x),numeros)))
    print("Ordenada:", sorted(numeros))
    print("Ordenada Reversa:", sorted(numeros,reverse=True))