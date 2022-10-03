
# Autor: Hincho Jove, Angel
# Programa que ayuda en el ingreso de calificaciones
# separadas por comas y las convierte en un valor entero

def ListaToEnteros(lista : list):
    try:
        listaInts = []
        for e in lista:
            listaInts.append(int(e))
        print(f"Lista con elementos de tipo Integer: {listaInts}")
        return listaInts
    except:
        print("¡Usted ingreso valores que no son enteros!")

def cadenaToLista(cadena : str):
    try:
        nums = []
        nums = cadena.split(',')
        print(f"Lista con elementos de tipo String: {nums}")
        return nums
    except:
        print("¡Ingresar una cadena respetando el formato de comas!")

def verificarComas(cadena : str):
    if (not(',' in cadena)):
        print("¡Ingresar una cadena respetando el formato de comas!")
    return (not(',' in cadena))

def ingresarCalificaciones():
    print("Dividir las calificaciones por comas ',' ...")
    ingresoComas = str(input("Ingrese una lista de calificaciones: "))
    flag = verificarComas(ingresoComas)
    while (flag):
        ingresoComas = str(input("Ingrese una lista de calificaciones: "))
        flag = verificarComas(ingresoComas)
    listaStrs = cadenaToLista(ingresoComas)
    ListaToEnteros(listaStrs)

def main():
    ingresarCalificaciones()

main()
