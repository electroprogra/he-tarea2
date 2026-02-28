'''
' ARACT - HACKING ETICO nivel 1 - 2026 Febrero
' Tarea 2 · Módulo 2: (GitHub + Python Básico + Port Scanner + Banner Grabber).
' @author el3ctroprogra@gmail.com
'''

import socket


### CONSTANTES ###
LOCALHOST = '127.0.0.1'
PORT_MIN = 1
PORT_MAX = 65535
puertosComunes = {
    "21": "ftp",
    "22": "ssh",
    "23": "telnet",
    "25": "smtp",
    "80": "http",
    "53": "dns",
    "69": "tftp",
    "123": "ntp",
    "110": "pop3",
    "143": "imap",
    "161": "snmp",
    "389": "ldap",
    "443": "https",
    "445": "smb",
    "3306": "mysql",
    "3389": "rdp",
    "4350": "vs-code",
    "5000": "macos-control-center",
    "5900": "vnc",
    "7000": "macos-control-center",
    "8080": "http-alt",
    "8443": "https-alt",
    "6379": "redis",
    "9200": "elasticsearch",
    "11211": "memcached",
    "27017": "mongodb",
    "58660": "python",
    "63506": "macos-rapportd",
}
###


'''
' @param justify: {"left", "center", "right"}
' @param boxCharCode: {char, "line", "doubleLine"}
'''
def ascii_title(title, hPadding=1, vPadding=0, justify="center", boxCharCode="line"):
    #Asegurar que el título sea una lista de cadenas
    title_array = []
    title_array_maxlength = 0
    if isinstance(title, list): title_array = title
    else: title_array = title.split("\n")

    for title_element in title_array:
        if len(title_element) > title_array_maxlength:
            title_array_maxlength = len(title_element)

    #ASCCI art para el borde
    if boxCharCode == "line":
        hLine = b'\xC4'.decode('cp437') #chr(196)
        vLine = b'\xB3'.decode('cp437') #chr(179)
        cornerTL = b'\xDA'.decode('cp437') #chr(218)
        cornerTR = b'\xBF'.decode('cp437') #chr(191)
        cornerBL = b'\xC0'.decode('cp437') #chr(192)
        cornerBR = b'\xD9'.decode('cp437') #chr(217)
    elif boxCharCode == "doubleLine":
        hLine = b'\xCD'.decode('cp437') #chr(205)
        vLine = b'\xBA'.decode('cp437') #chr(186)
        cornerTL = b'\xC9'.decode('cp437') #chr(201)
        cornerTR = b'\xBB'.decode('cp437') #chr(187)
        cornerBL = b'\xC8'.decode('cp437') #chr(200)
        cornerBR = b'\xBC'.decode('cp437') #chr(188)
    else:
        hLine = boxCharCode
        vLine = boxCharCode
        cornerTL = boxCharCode
        cornerTR = boxCharCode
        cornerBL = boxCharCode
        cornerBR = boxCharCode
    
    #Borde superior
    print(cornerTL, end="")
    for p in range(0, title_array_maxlength+hPadding*2, 1): print(hLine, end="")
    print(cornerTR)

    #Padding superior más segmentos de borde correspondientes
    for p in range(0, vPadding, 1):
        print(vLine, end="")
        for p in range(0, title_array_maxlength+hPadding*2, 1): print(" ", end="")
        print(vLine)
        
    #TITULO más segmentos de borde correspondientes
    for title_element in title_array:
        hPaddingByJustifyTotal = title_array_maxlength - len(title_element)
        print(vLine, end="")
        if justify == "left":
            for p in range(0, hPadding, 1): print(" ", end="")
            print(title_element, end="")
            for p in range(0, hPadding+hPaddingByJustifyTotal, 1): print(" ", end="")
        else: #justify == "center" por defecto
            hPaddingByJustify = int(hPaddingByJustifyTotal/2)
            #En el caso de que el padding necesario para centrar el title_element sea un numero impar,
            #se tendrá como resultado padding diferente a cada lado del title_element.
            for p in range(0, hPadding+hPaddingByJustify, 1): print(" ", end="")
            print(title_element, end="")
            #En el caso de que el padding necesario para centrar el title_element sea un numero impar,
            #se tendrá como resultado padding diferente a cada lado del title_element.
            for p in range(0, hPadding+hPaddingByJustifyTotal-hPaddingByJustify, 1): print(" ", end="")
        print(vLine)

    #Padding inferior más segmentos de borde correspondientes
    for p in range(0, vPadding, 1):
        print(vLine, end="")
        for p in range(0, title_array_maxlength+hPadding*2, 1): print(" ", end="")
        print(vLine)

    #Borde inferior
    print(cornerBL, end="")
    for p in range(0, title_array_maxlength+hPadding*2, 1): print(hLine, end="")
    print(cornerBR)


def scanPort(ip_objetivo, puerto, desc=""):
    try:
        socket_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultado = socket_conexion.connect_ex((ip_objetivo, puerto))
        
        if resultado == 0:
            print(f'Puerto {puerto} ({desc}): ABIERTO' if desc != "" else f'Puerto {puerto}: ABIERTO')
            
            # Intentamos obtener el banner
            try:
                socket_conexion.settimeout(2) # Timeout en segundos
                banner = socket_conexion.recv(1024)
                banner_texto = banner.decode('utf-8', errors='ignore')
                print(f'Banner: {banner_texto.strip()}' + '\n')
            except:
                print(f'Banner: No disponible' + '\n')
        
        socket_conexion.close()
    except:
        pass


ascii_title("Scanner.py v1.0\n\npor\nel3ctroprogra@gmail.com", 3, 1, "center", "doubleLine")
print()

ip_objetivo = input("Ingrese la dirección IP a escanear (Presiona   l   para usar localhost): ")
if ip_objetivo == 'l':
    ip_objetivo = LOCALHOST

puerto_inicio_str = input(f"Ingrese el puerto de inicio (entre {PORT_MIN} y {PORT_MAX}, escriba   tarea   para escanear del puerto 1 al 200, presiona   d   para usar puertos comunes): ")
### Escanear puertos comunes ###
if puerto_inicio_str == 'd':
    print(f'\nEscaneando {ip_objetivo} en puertos comunes...')
    print('-' * 50)

    for puerto_str, desc in puertosComunes.items():
        puerto = int(puerto_str)
        scanPort(ip_objetivo, puerto, desc)
###
else:
    #Se seleccionaron los puertos indicados en la tarea
    if puerto_inicio_str == 'tarea':
        puerto_inicio = 1
        puerto_fin = 200
    #Se seleccionaron puertos personalizados
    else:
        puerto_inicio = int(puerto_inicio_str)
        puerto_fin_str = input(f"Ingrese el puerto de fin (entre {puerto_inicio} y {PORT_MAX}, presiona   x   para usar el puerto final 65535): ")
        if puerto_fin_str == 'x':
            puerto_fin = PORT_MAX
        else:
            puerto_fin = int(puerto_fin_str)

    #Probar el rango de puertos seleccionado
    print(f'\nEscaneando {ip_objetivo} del puerto {puerto_inicio} a {puerto_fin}...')
    print('-' * 50)

    for puerto in range(puerto_inicio, puerto_fin + 1):
        scanPort(ip_objetivo, puerto)

print('-' * 50)    
print("Escaneo completado.")