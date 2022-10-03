
# Autor: Hincho Jove, Angel
# Modulo para generar numeros aleatorios en una lista

import random as rdm

def generarVeinteRandoms():
    aleatorios = []
    for i in range(0, 20):
        aleatorios.append(rdm.randint(0, 100))
    return aleatorios

def imprimirAleatorios(listaRdm : list):
    print(f"Lista de Aleatorios: {listaRdm}")

def ordernarAleatorios(listaRdm : list):
    listaRdm.sort()
    print(f"Lista Ordenada: {listaRdm}")
