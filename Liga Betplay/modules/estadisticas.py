def faltas(liga): 
    maxfaltas = 0
    jugadorFaltas = None

    for equipo in liga:
        for jugador in equipo["jugadores"]:
            if jugador["faltas"] > maxfaltas:
                maxfaltas = jugador["faltas"]
                jugadorFaltas = jugador["nombre"]

    if jugadorFaltas:
        print(f"El jugador que más faltas ha cometido es: {jugadorFaltas} con {maxfaltas} faltas.")
    else:
        print("No hay jugadores registrados.")

def tarjetasA(liga):
    maxTarjetas = 0
    jugadorTarjetas = None

    for equipo in liga:
        for jugador in equipo["jugadores"]:
            if jugador["tarjetas_amarillas"] > maxTarjetas:
                maxTarjetas = jugador["tarjetas_amarillas"]
                jugadorTarjetas = jugador["nombre"]

    if jugadorTarjetas:
        print(f"El jugador que más tarjetas amarillas ha recibido es: {jugadorTarjetas} con {maxTarjetas} tarjetas amarillas.")
    else:
        print("No hay jugadores registrados.")

def goles(liga):
    maxGoles = 0
    equipoMaxGoles = None

    for equipo in liga:
        golesEquipo = sum(jugador["goles"] for jugador in equipo["jugadores"])
        if golesEquipo > maxGoles:
            maxGoles = golesEquipo
            equipoMaxGoles = equipo["nombre"]

    if equipoMaxGoles:
        print(f"El equipo que más goles ha marcado es: {equipoMaxGoles} con {maxGoles} goles.")
    else:
        print("No hay equipos registrados.")

def golesContra(liga, partidos):
    golesContra = {equipo["nombre"]: 0 for equipo in liga}

    for partido in partidos:
        if partido["resultado"]:
            golesLocal, golesVisitante = map(int, partido["resultado"].split('-'))
            golesContra[partido["visitante"]] += golesLocal
            golesContra[partido["local"]] += golesVisitante

    equipoGolesContra = max(golesContra, key=golesContra.get)
    maxGolesContra = golesContra[equipoGolesContra]

    print(f"El equipo que presenta más goles en contra es: {equipoGolesContra} con {maxGolesContra} goles en contra.")
