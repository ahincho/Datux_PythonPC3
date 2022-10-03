
# Autor: Hincho Jove, Angel
# Archivo que implementa el modulo de GenerarAleatorios

import GenerarAleatorios as Randoms

def main():
    aleatorios = Randoms.generarVeinteRandoms()
    Randoms.imprimirAleatorios(aleatorios)
    Randoms.ordernarAleatorios(aleatorios)

main()
