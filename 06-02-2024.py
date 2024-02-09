
def escoger_genero(genero):
    if genero == 'M':
        return f'Masculino'
    elif genero == 'F':
        return f'Femenino'
    else:
        return f'Género no disponible'

genero = input('Ingrese M o F para seleccionar su género: ')

print(escoger_genero(genero))
