# x = "Python "
# y = "es "
# z = "asombroso"
#
# print(x+y+z)
#
# print('Ingrese datos en las siguientes consignas para realizar la suma')
# a = int(input('Ingrese el primer numero: '))
# b = int(input('Ingrese el segundo numero: '))
# resultado = a + b
#
# print(f'El resultado de la operación es: {resultado}')
#
# if resultado % 2 == 0:
#     print(resultado, 'es par')
# else:
#     print(resultado, 'es impar')
#
#
#
#
print('Ingrese sus datos en las siguientes consignas')
cedula = input('Número de cédula: ')
nombre = input('Nombre: ')
apellido = input('Apellido: ')
correo = input('Correo: ')

persona = [cedula, nombre, apellido, correo]

print(f'Datos ingresados: {persona}')
