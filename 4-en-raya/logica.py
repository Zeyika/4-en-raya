from tablero import tablero, filas, columnas

def ganar(ficha):

    # Horizontal
    for f in range(filas):
        for c in range(columnas-3):
            if tablero[f][c] == ficha and tablero[f][c+1] == ficha and tablero[f][c+2] == ficha and tablero[f][c+3] == ficha:
                return True

    # Vertical
    for c in range(columnas):
        for f in range(filas-3):
            if tablero[f][c] == ficha and tablero[f+1][c] == ficha and tablero[f+2][c] == ficha and tablero[f+3][c] == ficha:
                return True

    # Diagonal \
    for f in range(filas-3):
        for c in range(columnas-3):
            if tablero[f][c] == ficha and tablero[f+1][c+1] == ficha and tablero[f+2][c+2] == ficha and tablero[f+3][c+3] == ficha:
                return True

    # Diagonal /
    for f in range(3, filas):
        for c in range(columnas-3):
            if tablero[f][c] == ficha and tablero[f-1][c+1] == ficha and tablero[f-2][c+2] == ficha and tablero[f-3][c+3] == ficha:
                return True

    return False