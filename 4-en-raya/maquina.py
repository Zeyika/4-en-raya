import random

#dificultades
def movimiento_maquina(dificultad):

    if dificultad == "baja":    #baja
        col = random.randint(0,6)

    elif dificultad == "media": #media
        col = random.randint(0,6)

    else:
        col = random.randint(0,6)   #alta

    return col