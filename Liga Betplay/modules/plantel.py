equipos = {}

def addCuerpo(lstLiga: list):
    isAddTeam = True
    while isAddTeam:
        plantel = input('Ingrese el nombre del equipo para definir su plantel: ').strip().capitalize()
        if plantel in lstLiga:
            cuerpoRegistrado = False
            for equipo in lstLiga:
                if isinstance(equipo, dict) and equipo["equipo"] == plantel:
                    cuerpoRegistrado = True
                    print(f'El cuerpo técnico del equipo {plantel} ya está registrado.')
                    break
            if not cuerpoRegistrado: #Solicita al usuario todo el plantel por equipo y lo almacena en lista
                tecnico = input("Ingrese el nombre del técnico: ").strip().capitalize()
                asistente = input("Ingrese el nombre del asistente técnico: ").strip().capitalize()
                preparadorFisico = input("Ingrese el nombre del preparador físico: ").strip().capitalize()
                medico = input("Ingrese el nombre del médico: ").strip().capitalize()
                cuerpoTecnico = {
                    "equipo": plantel,
                    "técnico": tecnico,
                    "asistente": asistente,
                    "preparador físico": preparadorFisico,
                    "médico": medico
                }
                equipos[plantel] = {"cuerpo_tecnico": cuerpoTecnico, "jugadores": []}
                print(f"Cuerpo técnico de {plantel} registrado con éxito.")
        else:
            print('El equipo no está registrado, regístrelo primero.')
        continuar = input("¿Desea agregar el plantel de otro equipo? S(Sí) N(No): ").strip().lower()
        if continuar == 'n':
            isAddTeam = False
        elif continuar != 's':
            print('Opción inválida, intente de nuevo.')

def listarJugadores(lstLiga: list):
    isAddPlayers = True
    while isAddPlayers:
        equipo = input('Ingrese el nombre del equipo para agregar jugadores: ').strip().capitalize()

        if equipo in equipos:
            agregarJugadores = input(f"¿Desea agregar jugadores para el equipo {equipo}? S(Sí) N(No): ").strip().lower()
            if agregarJugadores == 'n':
                isAddPlayers = False
                break
            elif agregarJugadores != 's':
                print('Opción inválida, intente de nuevo.')
                continue

            while True: #Solicita al usuario los jugadores por equipo y lo almacena en lista
                nombreJugador = input('Ingrese el nombre del jugador: ').strip().capitalize()
                posicion = input('Ingrese la posición del jugador: ').strip().capitalize()

                equipos[equipo]["jugadores"].append({
                    "nombre": nombreJugador,
                    "posición": posicion,
                    "goles": 0,
                    "tarjetas_amarillas": 0,
                    "tarjetas_rojas": 0,
                    "faltas": 0
                })
                print(f"Jugador {nombreJugador} registrado exitosamente en el equipo {equipo}.")

                agregarOtro = input("¿Desea agregar otro jugador? S(Sí) N(No): ").strip().lower()
                if agregarOtro == 'n':
                    break
                elif agregarOtro != 's':
                    print('Opción inválida, intente de nuevo.')

        else:
            print(f'El equipo {equipo} no está registrado. Registre el equipo primero.')
        
        continuar = input("¿Desea agregar jugadores para otro equipo? S(Sí) N(No): ").strip().lower()
        if continuar == 'n':
            isAddPlayers = False
        elif continuar != 's':
            print('Opción inválida, intente de nuevo.')
