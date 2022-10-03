
# Autor: Hincho Jove, Angel
# Programa para controlar el nivel de gasolina en un vehiculo

def calcularPorcentaje():
    while True:
        try:
            valorX = int(input("Ingrese el valor de X: "))
            valorY  = int(input("Ingrese el valor de Y: "))
            porcentaje = int(valorX * 100 / valorY)
            while(valorX > valorY):
                print("¡El valor de X debe ser menor o igual al valor de Y!")
                valorX = int(input("Ingrese el valor de X: "))
                valorY  = int(input("Ingrese el valor de Y: "))
            if (porcentaje < 1):
                print("Porcentaje: E")
            elif (porcentaje > 99):
                print("Porcentaje: F")
            else:
                print(f"Porcentaje: {porcentaje}%")
            break
        except ValueError:
            print("¡Ingrese números enteros!")
        except ZeroDivisionError:
            print("¡El valor de Y no puede ser igual a 0!")

def main():
    calcularPorcentaje()

main()
