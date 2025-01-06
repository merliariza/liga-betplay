import os
import modules.validate as val

def addTeam(lstLiga: list):
    isAddTeam = True
    nombreTeam = input('Ingrese el nombre del equipo participante: ').strip().capitalize()
    if nombreTeam in lstLiga:  
        isAddTeam = False
        print('El equipo ya está registrado')
        os.system('pause')
    while isAddTeam:
        lstLiga.append(nombreTeam)  #Si se añade un equipo se agrega a la lista.
        print(f"Equipo '{nombreTeam}' agregado a la liga.")
        agregarOtro = val.validateData('¿Desea agregar otro equipo? S(Sí) N(No)') 
        if not agregarOtro:  
            break
        else:
            nombreTeam = input('Ingrese el nombre del equipo participante: ').strip().capitalize()
            if nombreTeam in lstLiga:
                print('El equipo ya está registrado')
                os.system('pause')
                isAddTeam = False

def deleteTeam(lstLiga):
    isDeleteTeam = True
    while isDeleteTeam:
        teamName = input('Digite el nombre del equipo que desea eliminar: ')
        for team in lstLiga:
            if teamName == team[0]:  #Lee si el equipo ingresado por el usuario, fue registrado, si es así, lo elimina con remove()
                lstLiga.remove(team)  
                print(f'El equipo {teamName} ha sido eliminado.')
                isDeleteTeam = False
                return  
        print('El equipo no existe, primero cree el equipo.')
        return

def searchTeam(lstLiga):
    buscarEquipo = input('Ingrese el nombre del equipo que desea buscar: ')
    for team in lstLiga:
        if len(team) > 0 and buscarEquipo == team[0]:  #Lee si el equipo ingresado por el usuario, fue registrado, si es así, imprime: el equipo está registrado
            print(f'El equipo "{buscarEquipo}" está registrado.')
            return
    print(f'El equipo "{buscarEquipo}" no está registrado.')
    return