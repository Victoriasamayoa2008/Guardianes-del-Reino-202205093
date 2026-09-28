import random
import time

"""
GUARDIANES DEL REINO

Objeto: Jugador y Enemigo
Atributos: vidas, monedas, nivel, daño
Métodos: atacar(), jugar()
"""


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vidas = 100
        self.monedas = 0
        self.nivel = 1

    def atacar(self, enemigo, daño):
        print("\n" + self.nombre + " prepara su espada...")
        time.sleep(1)
        print("¡ATACA!")
        time.sleep(1)
        print("Daño realizado:", daño)

        enemigo.vidas -= daño

        print("Vida del enemigo:", max(enemigo.vidas, 0))


class Enemigo:
    def __init__(self, nivel):
        self.nombre = random.choice(
            ["Goblin", "Orco", "Dragon", "Caballero oscuro"]
        )
        self.vidas = 60 + nivel * 10

    def atacar(self, jugador):
        daño = random.randint(5, 15)

        print("\nEl", self.nombre, "contraataca...")
        time.sleep(1)
        print("Daño recibido:", daño)

        jugador.vidas -= daño

        print("Tus vidas:", max(jugador.vidas, 0))


def jugar():

    nombre = input("Escribe el nombre de tu guerrero: ")

    jugador = Jugador(nombre)

    print("\n================================")
    print("      GUARDIANES DEL REINO")
    print("================================")

    print("\nBienvenido,", jugador.nombre)

    while jugador.nivel <= 10 and jugador.vidas > 0:

        enemigo = Enemigo(jugador.nivel)

        print("\n--------------------------------")
        print("NIVEL:", jugador.nivel)
        print("ENEMIGO:", enemigo.nombre)
        print("VIDA:", enemigo.vidas)
        print("--------------------------------")

        while enemigo.vidas > 0 and jugador.vidas > 0:

            print("\n1. Atacar")

            opcion = input("Elige: ")

            if opcion == "1":

                # AQUÍ APARECEN LOS ATAQUES
                print("\nElige la fuerza de tu ataque:")
                print("10")
                print("15")
                print("20")
                print("25")

                ataque = input("Escribe el número de ataque: ")

                if ataque == "10":
                    daño = 10

                elif ataque == "15":
                    daño = 15

                elif ataque == "20":
                    daño = 20

                elif ataque == "25":
                    daño = 25

                else:
                    print("\nNúmero incorrecto.")
                    continue

                jugador.atacar(enemigo, daño)

                if enemigo.vidas <= 0:

                    print("\nHas derrotado al", enemigo.nombre)

                    monedas = random.randint(10, 30)
                    jugador.monedas += monedas

                    print("Ganaste", monedas, "monedas.")

                    jugador.nivel += 1

                    time.sleep(2)

                else:

                    enemigo.atacar(jugador)

                    time.sleep(2)

            else:
                print("\nDebes escribir 1 para atacar.")

    if jugador.vidas <= 0:

        print("\nGAME OVER")
        print("Has perdido todas tus vidas.")

    else:

        print("\nFELICIDADES,", jugador.nombre)
        print("Has completado los 10 niveles.")
        print("Has salvado el Reino.")


jugar()
