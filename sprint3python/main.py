# main.py
from heroe import Heroe
from mazmorra import Mazmorra

if __name__ == "__main__":
    nombre = input("Introduce el nombre de tu héroe: ")
    heroe = Heroe(nombre)
    mazmorra = Mazmorra(heroe)
    mazmorra.jugar()