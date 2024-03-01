import socket
import sys

def checkPortsSocket(ip, portlist):
    try:
        for port in portlist:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print("Puerto {}: \t Abierto".format(port))
            else:
                print("Puerto {}: \t Cerrado".format(port))
            sock.close()
    except socket.error as error:
        print(str(error))






import urllib3


pool = urllib3.PoolManager(10)
response = pool.request('GET','http://www.tes.edu.ec')
# print(response.data)
print(response.getheaders())
python -m pip install requests



respuesta = requests.get('https://www.tes.edu.ec')
print(respuesta)
print(respuesta.text)
print(respuesta.text.find('Admisiones'))


