from modo1 import modo_un_jugador
from modo2 import modo_dos_jugadores

modo = input("Modo (1 = 1 jugador / 2 = 2 jugadores): ")

if modo == "1":

    dificultad = input("Dificultad (baja / media / alta): ")

    while dificultad not in ["baja", "media", "alta"]:
        print("Error")
        dificultad = input("Dificultad (baja / media / alta): ") 
    
    modo_un_jugador(dificultad)

elif modo == "2":
    modo_dos_jugadores()

else:
    print("Error")