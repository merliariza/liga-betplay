import modules.plantel as pl

partidos = []

def programar(lstLiga):
    if len(lstLiga) < 2:
        print("Debe haber al menos dos equipos registrados para programar un partido.")
        return

    equipoL = input('Ingrese el nombre del equipo local: ').strip().capitalize()
    equipoV = input('Ingrese el nombre del equipo visitante: ').strip().capitalize()
    
    if equipoL not in lstLiga:
        print('El equipo local que usted desea ingresar no está registrado, regístrelo primero.')
        return
    if equipoV not in lstLiga:
        print('El equipo visitante que usted desea ingresar no está registrado, regístrelo primero.')
        return
    if equipoL == equipoV:
        print('El equipo no puede jugar contra sí mismo.')
        return

    dia = input('Ingrese un día: ')
    mes = input('Ingrese un mes: ')
    año = input('Ingrese un año: ')
    hora = input('Ingrese la hora: ')
    
   
    try:
        fecha = f'{dia}/{mes}/{año}'

    except ValueError:
        print("Fecha inválida. Asegúrese de ingresar números válidos.")
        return
    
    print(f'El {equipoL} vs {equipoV} están programados para la siguiente fecha: {fecha} a las {hora} hrs.')
    
    partidos.append({
        'local': equipoL,
        'visitante': equipoV,
        'fecha': fecha,
        'resultado': None  
    })    

def registrarResultados(lstJugadores):
    if not partidos:
        print("No hay partidos programados.")
        return
    
    print("Partidos programados:")
    for i, partido in enumerate(partidos, 1):
        print(f"{i}. {partido['local']} vs {partido['visitante']} - {partido['fecha']}")

    try:
        seleccion = int(input("Seleccione el número del partido para registrar el resultado: ")) - 1
        if 0 <= seleccion < len(partidos):
            partido = partidos[seleccion]
            if partido['resultado']:
                sobrescribir = input("Este partido ya tiene un resultado registrado. ¿Desea sobrescribirlo? (s/n): ").lower()
                if sobrescribir != 's':
                    print("Registro de resultado cancelado.")
                    return

            registrarResultadosJugadores(partido)

            golesLocal = int(input(f"Goles de {partido['local']}: "))
            golesVisitante = int(input(f"Goles de {partido['visitante']}: "))
            
            partido['resultado'] = f"{golesLocal}-{golesVisitante}"
            print(f"Resultado registrado: {partido['local']} {golesLocal} - {golesVisitante} {partido['visitante']}")
    
        else:
            print("Selección inválida.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

def registrarResultadosJugadores(partido):
    equipos = [partido['local'], partido['visitante']]
    for equipo in equipos:
        print(f"\nRegistrar estadísticas para el equipo: {equipo}")
        try:
            jugadores = pl.equipos[equipo]["jugadores"] 
        except KeyError:
            print(f"No se encontraron jugadores para el equipo {equipo}.")
            continue
        
        for jugador in jugadores:
            nombreJugador = jugador["nombre"]
            print(f"\nJugador: {nombreJugador}")
            try:
                goles = int(input(f"Ingrese los goles anotados por {nombreJugador}: "))
                tarjetasAmarillas = int(input(f"Ingrese las tarjetas amarillas de {nombreJugador}: "))
                tarjetasRojas = int(input(f"Ingrese las tarjetas rojas de {nombreJugador}: "))
                faltas = int(input(f"Ingrese las faltas cometidas por {nombreJugador}: "))
                
                jugador["goles"] += goles
                jugador["tarjetas_amarillas"] += tarjetasAmarillas
                jugador["tarjetas_rojas"] += tarjetasRojas
                jugador["faltas"] += faltas
                
                print(f"Estadísticas de {nombreJugador} actualizadas: Goles: {jugador['goles']}, Tarjetas Amarillas: {jugador['tarjetas_amarillas']}, Tarjetas Rojas: {jugador['tarjetas_rojas']}, Faltas: {jugador['faltas']}")
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números válidos.")
                continue

def imprimirResultados():
    if not partidos:
        print("No hay partidos programados.")
        return

    for partido in partidos:
        print(f"\nPartido: {partido['local']} vs {partido['visitante']} - Resultado: {partido['resultado']}, Fecha: {partido['fecha']}")
