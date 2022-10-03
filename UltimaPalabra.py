
# Autor: Hincho Jove, Angel Eduardo
# Programa que devuelve la longitud de la
# ultima palabra en una cadena ingresada

def ultimaPalabra():
    while True:
        try:
            cadena = str(input("Ingrese una o más palabras: "))
            palabras = cadena.split(" ")
            # Limpiando posibles espacios demas
            while ('' in palabras):
                palabras.remove('')
            lastIndex = len(palabras) - 1
            print(f'Palabras ingresadas: {palabras}')
            print(f"Su última palabra ingresada es: {palabras[lastIndex]}")
            print(f"Longitud de la última palabra ingresada: {len(palabras[lastIndex])}")
            break
        except ValueError:
            print("¡Debe ingresar solo palabras!")

def main():
    ultimaPalabra()

main()
