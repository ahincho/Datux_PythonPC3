
# Autor: Hincho Jove, Angel
# Modulo que contiene operaciones numéricas básicas

def sumar(a : float, b : float):
    while True:
        try:
            print("¡Suma!")
            print(f"{a} + {b} = ?")
            return (a + b)
        except:
            print("¡Debes ingresar dos números!")
            a = float(input(f"Ingrese un número que reemplace el valor de {a}: "))
            b = float(input(f"Ingrese un número que reemplace el valor de {b}: "))

def restar(a : float, b : float):
    while True:
        try:
            print("¡Resta!")
            print(f"{a} - {b} = ?")
            return (a - b)
        except:
            print("¡Debes ingresar dos números!")
            a = float(input(f"Ingrese un número que reemplace el valor de {a}: "))
            b = float(input(f"Ingrese un número que reemplace el valor de {b}: "))

def multiplicar(a : float, b : float):
    while True:
        try:
            print("¡Multiplicación!")
            print(f"{a} * {b} = ?")
            return (a * b)
        except:
            print("¡Debes ingresar dos números!")
            a = float(input(f"Ingrese un número que reemplace el valor de {a}: "))
            b = float(input(f"Ingrese un número que reemplace el valor de {b}: "))

def dividir(a : float, b : float):
    while True:
        try:
            print("¡División!")
            print(f"{a} / {b} = ?")
            return (a / b)
        except ZeroDivisionError:
            print("¡No se permite la divisón entre 0!")
            b = float(input(f"Ingrese un número que reemplace el valor de {b}: "))
        except:
            print("¡Debes ingresar dos números!")
            a = float(input(f"Ingrese un número que reemplace el valor de {a}: "))
            b = float(input(f"Ingrese un número que reemplace el valor de {b}: "))
