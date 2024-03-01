import sys
def validar_ip(ip):
    octetos = ip.split('.')
    if len(octetos) != 4:
        return False
    for octeto in octetos:
        try:
            valor = int(octeto)
            if valor < 0 or valor > 255:
                return False
        except ValueError:
            return False
    return True

def clase_ip(ip):
    octetos = list(map(int, ip.split('.')))
    if 1 <= octetos[0] <= 126:
        return 'A'
    elif 128 <= octetos[0] <= 191:
        return 'B'
    elif 192 <= octetos[0] <= 223:
        return 'C'
    else:
        return 'No es A, B o C'

def validar_direccion_ip(ip, clase):
    clase = clase.upper()  # Convertir a mayúsculas
    if clase.startswith("CLASE "):
        clase = clase[6:]  # Eliminar "CLASE " si está presente
    clase_ip_calculada = clase_ip(ip)
    if clase_ip_calculada == clase:
        return f'La dirección IP {ip} corresponde a la clase {clase}.'
    else:
        return f'La dirección IP {ip} no corresponde a la clase {clase}. Pertenece a la clase {clase_ip_calculada}.'

def main():
    if len(sys.argv) != 3:
        print("Uso: python script.py <direccion_ip> <clase>")
        sys.exit(1)

    ip = sys.argv[1]
    clase = sys.argv[2]

    if not validar_ip(ip):
        print("La dirección IP ingresada no es válida.")
        sys.exit(1)

    print(validar_direccion_ip(ip, clase.upper()))

if __name__ == "__main__":
    main()