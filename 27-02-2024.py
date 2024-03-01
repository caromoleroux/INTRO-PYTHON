import sys

if len(sys.argv) != 3:
    print(f'Uso: {sys.argv[0]} <nombre> <accion|lower-upper-title>')
    sys.exit()

usr_nombre = sys.argv[1]
usr_accion = sys.argv[2] #lower-upper-title

if usr_accion == 'lower':
    print(f'{usr_nombre.lower()}')
elif usr_accion == 'upper':
    print(f'{usr_nombre.upper()}')
elif usr_accion == 'title':
    print(f'{usr_nombre.title()}')
else:
    print('Accion no es válida')