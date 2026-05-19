import random

#dificultades
def movimiento_maquina(dificultad):

    if dificultad == "baja":    #baja
        col = random.randint(0,6)

    elif dificultad == "media": #media
        col = random.randint(0,6)

    elif dificultad == "alta":  #alta
        col = random.randint(0,6)   

    else:
        print("Error")   
        return None
    
    return col