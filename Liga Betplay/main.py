import os
import modules.ui as ui
import modules.mensajes as msg
import modules.validate as val
import modules.plantel as pl
import modules.menu as mn
import modules.programar as pm
import modules.estadisticas as es

isActive = True

if __name__ == "__main__":
    ligaBetplay = []

    while isActive:
        try:
            os.system('cls')
            print(msg.titulo)
            print(ui.menu)
            opcMenu = int(input(':)_'))
#Se establece un match para el menú principal, donde cada caso representa una función del menú, de la misma forma con cada menú.
            match opcMenu:
                case 1:  
                    isAddTeam = True
                    while isAddTeam:
                        try:
                            os.system('cls')
                            print(msg.tituloMenuEquipos)
                            print(ui.menuEquipos)
                            opcMenuTeam = int(input(':)_'))

                            match opcMenuTeam:#Da las opciones por casos: agregar equipo, eliminar equipo y buscar equipo
                                case 1:
                                    mn.addTeam(ligaBetplay)
                                    print('Los equipos registrados son:')
                                    print(ligaBetplay)
                                    os.system('pause')
                                case 2:
                                    mn.deleteTeam(ligaBetplay)
                                    os.system('pause')
                                case 3:
                                    mn.searchTeam(ligaBetplay)
                                    os.system('pause')
                                case 4:
                                    input("Presione enter para ser dirigido al menú principal")
                                    break
                                case _:
                                    print('La opción ingresada es inválida')
                                    os.system('pause')
                        except ValueError:
                            print('El dato ingresado es inválido')
                            os.system('pause')

                case 2: 
                    isAddPlantel = True
                    while isAddPlantel:
                        try:
                            os.system('cls')
                            print(msg.tituloMenuPlantel)
                            print(ui.menuPlantel)
                            opcMenuPlantel = int(input(':)_'))

                            match opcMenuPlantel: #Establece por casos las opciones añadir plantel y listar jugadores.
                                case 1:
                                    pl.addCuerpo(ligaBetplay)
                                    print('Los equipos registrados son: ')
                                    print(ligaBetplay)
                                    os.system('pause')
                                case 2:
                                    pl.listarJugadores(ligaBetplay)
                                    os.system('pause')
                                case 3:
                                    input("Presione enter para ser dirigido al menú principal")
                                    break
                                case _:
                                    print('La opción ingresada es inválida')
                                    os.system('pause')
                        except ValueError:
                            print('El dato ingresado es inválido')
                            os.system('pause')

                case 3:
                    isProgramar = True
                    while isProgramar:
                        try:
                            os.system('cls')
                            print(msg.tituloMenuProgramar)
                            print(ui.menuProgramar)
                            opcMenuProgramar = int(input(':)_'))

                            match opcMenuProgramar: #Da las opciones por casos: programar partido, registrar resultados, imprimir resultados.
                                case 1:
                                    pm.programar(ligaBetplay)
                                    os.system('pause')
                                case 2:
                                    pm.registrarResultados(ligaBetplay)
                                    os.system('pause')
                                case 3:
                                    pm.imprimirResultados()
                                    os.system('pause')
                                case 4:
                                    input("Presione enter para ser dirigido al menú principal")
                                    break
                                case _:
                                    print('La opción ingresada es inválida')
                                    os.system('pause')
                        except ValueError:
                            print('El dato ingresado es inválido')
                            os.system('pause')

                case 4:  
                    isEstadisticas = True
                    while isEstadisticas:
                        try:
                            os.system('cls')
                            print(msg.tituloMenuEstadisticas)
                            print(ui.menuEstadisticas)
                            opcMenuEstadisticas = int(input(':)_'))

                            match opcMenuEstadisticas:#Muestra las estadisticas por jugadores y equipos registrados en el plantel.
                                case 1:
                                    es.goles(ligaBetplay)
                                    os.system('pause')
                                case 2:
                                    es.golesContra(ligaBetplay)
                                    os.system('pause')
                                case 3:
                                    es.faltas(ligaBetplay)
                                    os.system('pause')
                                case 4:
                                    es.tarjetasA(ligaBetplay)
                                    os.system('pause')
                                case 5:
                                    input("Presione enter para ser dirigido al menú principal")
                                    break
                                case _:
                                    print('La opción ingresada es inválida')
                                    os.system('pause')
                        except ValueError:
                            print('El dato ingresado es inválido')
                            os.system('pause')

                case 5:  
                    isActive = val.validateData(msg.msgInfoAddTeam)

                case _:
                    print('La opción ingresada es inválida')
                    os.system('pause')

        except ValueError:
            print('Error en el dato ingresado')
            os.system('pause')