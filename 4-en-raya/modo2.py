from tablero import mostrar_tablero, colocar_ficha
from logica import ganar

def modo_dos_jugadores():
    juego = True
    turno = "X"

    while juego:

        mostrar_tablero()

        col = int(input("Turno " + turno + " (0-6): "))
        colocar_ficha(col, turno)

        if ganar(turno):
            mostrar_tablero()
            print("Gana " + turno)
            juego = False

        if turno == "X":
            turno = "O"
        else:
            turno = "X"