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
clase = clase_ip(ip)
print(f"La dirección IP {ip} pertenece a la {clase}.")
