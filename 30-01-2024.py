#Ejercicio de año bisiesto
x = int(input('Ingrese un año: '))
if x % 4 == 0 and x % 100 != 0:
    print(f'{x} es año bisiesto')
else:
    print(f'{x} no es año bisiesto')
