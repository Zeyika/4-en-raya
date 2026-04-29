filas = 6
columnas = 7

tablero = [[" " for i in range(columnas)] for j in range(filas)]

def mostrar_tablero():
    print()
    for fila in tablero:
        print("|", end="")
        for casilla in fila:
            print(casilla + "|", end="")
        print()
    print(" 0 1 2 3 4 5 6")

def colocar_ficha(col, ficha):
    for f in range(filas-1, -1, -1):
        if tablero[f][col] == " ":
            tablero[f][col] = ficha
            return True
    return False