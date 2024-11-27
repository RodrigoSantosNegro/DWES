from tesoro import Tesoro
from monstruo import Monstruo

class Mazmorra:
    def __init__(self, heroe):
        self.heroe = heroe
        self.monstruos = [
            Monstruo("Esqueleto", 8, 3, 30),
            Monstruo("Orco", 12, 5, 50),
            Monstruo("Dragón", 20, 10, 100)
        ]
        self.tesoro = Tesoro()

    def jugar(self):
        print("Héroe entra en la mazmorra.")
        for monstruo in self.monstruos:
            print(f"\nTe has encontrado con un {monstruo.nombre}.")
            self.enfrentar_enemigo(monstruo)
            if not self.heroe.esta_vivo():
                print("Héroe ha sido derrotado en la mazmorra.")
                return
            self.buscar_tesoro()

        print(f"¡{self.heroe.nombre} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")

    def enfrentar_enemigo(self, enemigo):
        while enemigo.esta_vivo() and self.heroe.esta_vivo():
            print("\n¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Defender")
            print("3. Curarse")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.heroe.atacar(enemigo)
            elif opcion == "2":
                self.heroe.defenderse()
            elif opcion == "3":
                self.heroe.curarse()
            else:
                print("Opción no válida.")

            if enemigo.esta_vivo():
                enemigo.atacar(self.heroe)

            self.heroe.reset_defensa()

    def buscar_tesoro(self):
        print("\nBuscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe)