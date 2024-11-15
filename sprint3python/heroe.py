class Heroe:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = 10
        self.defensa = 5
        self.salud = 100
        self.salud_maxima = 100
        self.defensa_temporal = 0  # Para almacenar el aumento temporal

    def atacar(self, enemigo):
        daño = max(self.ataque - enemigo.defensa, 0)
        if daño > 0:
            enemigo.salud -= daño
            print(f"Héroe ataca a {enemigo.nombre}.")
            print(f"El enemigo {enemigo.nombre} ha recibido {daño} puntos de daño.")
        else:
            print(f"El enemigo ha bloqueado el ataque.")

    def curarse(self):
        curacion = 20
        self.salud = min(self.salud + curacion, self.salud_maxima)
        print(f"Héroe se ha curado. Salud actual: {self.salud}")

    def defenderse(self):
        self.defensa_temporal = 5
        print(f"Héroe se defiende. Defensa aumentada temporalmente a {self.defensa + self.defensa_temporal}.")

    def reset_defensa(self):
        if self.defensa_temporal > 0:
            print(f"La defensa de {self.nombre} vuelve a la normalidad.")
            self.defensa_temporal = 0

    def esta_vivo(self):
        return self.salud > 0