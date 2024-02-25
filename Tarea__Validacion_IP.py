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
        return 'Clase A'
    elif 128 <= octetos[0] <= 191:
        return 'Clase B'
    elif 192 <= octetos[0] <= 223:
        return 'Clase C'
    else:
        return 'No es clase A, B o C'

ip = input("Ingresa la dirección IP: ")

if validar_ip(ip):
    clase = clase_ip(ip)
    print(f"La dirección IP {ip} pertenece a la {clase}.")
else:
    print("La dirección IP ingresada no es válida.")
