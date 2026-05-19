from tablero import mostrar_tablero, colocar_ficha
from logica import ganar

def modo_dos_jugadores():
    juego = True
    turno = "X"

    while juego:

        mostrar_tablero()

        entrada = input("Turno " + turno + " (0-6): ")

        while entrada not in ["0","1","2","3","4","5","6"]:
            print("Error")
            entrada = input("Turno " + turno + " (0-6): ")

        col = int(entrada)

        while not colocar_ficha(col, turno):
            print("Columna llena")
            entrada = input("Turno " + turno + " (0-6): ")

            while entrada not in ["0","1","2","3","4","5","6"]:
                print("Error")
                entrada = input("Turno " + turno + " (0-6): ")

            col = int(entrada)

        if ganar(turno):
            mostrar_tablero()
            print("Gana " + turno)
            juego = False

        if turno == "X":
            turno = "O"
        else:
            turno = "X"