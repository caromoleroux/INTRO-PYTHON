
conjunto_cedula = set()
for _ in range(5):
    cedula = input("Ingrese su cédula: ")

    if len(cedula) == 10 and cedula.isdigit():
        conjunto_cedula.add(cedula)
    else:
        print("Error: La cédula debe contener 10 dígitos numéricos.")

print("Conjunto de cédulas ingresadas:", conjunto_cedula)

