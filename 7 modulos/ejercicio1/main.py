from calculadora import suma, resta, multiplicacion as mul, divicion as div

def main():
    print("Suma:", suma.sum(3,6))
    print("Resta:", resta.res(3,6))
    print("Multiplicacion:", mul.multi(3,6))
    print("Divicion:", div.divi(3,6))

if __name__ == '__main__':
    main()