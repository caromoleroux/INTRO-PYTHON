import random

def generar_direccion_ip(clase):
    if clase == 'A':
        primer_octeto = random.randint(1, 126)
    elif clase == 'B':
        primer_octeto = random.randint(128, 191)
    elif clase == 'C':
        primer_octeto = random.randint(192, 223)
    else:
        raise ValueError("Clase de dirección IP no válida")

    ip = f"{primer_octeto}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    return ip

def generar_direcciones_ips(cantidad, clase):
    direcciones_ips = []
    for _ in range(cantidad):
        direcciones_ips.append(generar_direccion_ip(clase))
    return direcciones_ips

cantidad = int(input("Ingresa la cantidad de direcciones IP que deseas generar: "))
clase = input("Ingresa la clase de direcciones IP que deseas generar (A, B o C): ").upper()

if clase not in {'A', 'B', 'C'}:
    print("Clase de dirección IP no válida. Debe ser 'A', 'B' o 'C'.")
else:
    direcciones_generadas = generar_direcciones_ips(cantidad, clase)
    print(f"\nDirecciones IP generadas de clase {clase}:")
    for direccion in direcciones_generadas:
        print(direccion)
