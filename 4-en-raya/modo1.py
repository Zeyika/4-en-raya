from tablero import mostrar_tablero, colocar_ficha
from logica import ganar
from maquina import movimiento_maquina

def modo_un_jugador(dificultad):
    juego = True

    while juego:

        mostrar_tablero()

        entrada = input("Tu turno (0-6): ")

        while entrada not in ["0","1","2","3","4","5","6"]:
            print("Error")
            entrada = input("Tu turno (0-6): ")

        col = int(entrada)

        while not colocar_ficha(col, "X"):
            print("Columna llena")
            entrada = input("Tu turno (0-6): ")

            while entrada not in ["0","1","2","3","4","5","6"]:
                print("Error")
                entrada = input("Tu turno (0-6): ")

            col = int(entrada)

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