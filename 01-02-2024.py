from EMPLEADOS import EMPLEADOS
# # cantidad = len(empleados)
# # print(cantidad)
#
# for empleado in empleados:
#   print(empleado)
cantidad = len(EMPLEADOS)
suma = 0

for empleado in EMPLEADOS:
    suma += empleado["age"]
promedio = suma / cantidad
print(f"El promedio es: {promedio}")