from tablero import mostrar_tablero, colocar_ficha
from logica import ganar
from maquina import movimiento_maquina

def modo_un_jugador(dificultad):
    juego = True

    while juego:

        mostrar_tablero()

        col = int(input("Tu turno (0-6): "))
        colocar_ficha(col, "X")

        if ganar("X"):
            mostrar_tablero()
            print("Has ganado")
            juego = False

        if juego:
            col = movimiento_maquina(dificultad)
            colocar_ficha(col, "O")

            if ganar("O"):
                mostrar_tablero()
                print("Gana la maquina")
                juego = False