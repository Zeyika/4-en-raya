from modo2 import modo_dos_jugadores

modo = input("Modo (1 = 1 jugador / 2 = 2 jugadores): ")

if modo == "1":
    dificultad = input("Dificultad (baja / media / alta): ")
    modo_un_jugador(dificultad)
else:
    modo_dos_jugadores()