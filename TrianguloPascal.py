
# Autor: Hincho Jove, Angel
# Programa que crea el triangulo de Pascal de base 'n'

def printTriangulo(triangulo : list):
    base = len(triangulo)
    for i in range(0, base):
        linea = ""
        for j in range(0, len(triangulo[i]) - 1):
            if(j == len(triangulo[i]) - 1):
                linea += str(triangulo[i][j])
            else:
                linea += (str(triangulo[i][j]) + " ")
        linea += str(triangulo[i][len(triangulo[i]) - 1])
        print(linea.center(100, " "))

def crearTriangulo(base : int):
    triangulo = []
    contador = 0
    while (contador < base):
        fila = []
        if(contador < 2):
            for i in range(0, contador + 1):
                fila.append(1)
        else:
            fila.append(1)
            for i in range(0, contador - 1):
                valorCalculado = triangulo[contador - 1][i] + triangulo[contador - 1][i + 1]
                fila.append(valorCalculado)
            fila.append(1)
        triangulo.append(fila)
        contador += 1
    return triangulo

def trianguloPascal():
    while True:
        try:
            base = int(input("Ingrese el valor de la base del triangulo: "))
            triangulo = crearTriangulo(base)
            printTriangulo(triangulo)
            break
        except ValueError:
            print("¡Ingresar un número entero!")

def main():
    trianguloPascal()

main()
