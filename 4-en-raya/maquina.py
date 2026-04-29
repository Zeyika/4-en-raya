import random

def movimiento_maquina(dificultad):

    if dificultad == "baja":
        col = random.randint(0,6)

    elif dificultad == "media":
        col = random.randint(0,6)

    else:
        col = random.randint(0,6)

    return col