def validateData(message: str): 
    opciones = ('N', 'n', 'S', 's') 
    while True:  
        accion = input(f'{message} : ').strip() 
        if accion not in opciones:  
            print('La opción que ingresó no está permitida, por favor intente de nuevo.')
        else:
            return accion.lower() == 's'  