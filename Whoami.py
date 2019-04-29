"""
 [] Script for devops
 [] Verificação de portas em uso e abertura de portas via linha de comando
 [] Create by: Gustavo Neri
"""

import platform, socket, sys

print ('''
                                                                                       
I8,        8        ,8I  88                                                        88  
`8b       d8b       d8'  88                                                        ""  
 "8,     ,8"8,     ,8"   88                                                            
  Y8     8P Y8     8P    88,dPPYba,    ,adPPYba,   ,adPPYYba,  88,dPYba,,adPYba,   88  
  `8b   d8' `8b   d8'    88P'    "8a  a8"     "8a  ""     `Y8  88P'   "88"    "8a  88  
   `8a a8'   `8a a8'     88       88  8b       d8  ,adPPPPP88  88      88      88  88  
    `8a8'     `8a8'      88       88  "8a,   ,a8"  88,    ,88  88      88      88  88  
     `8'       `8'       88       88   `"YbbdP"'   `"8bbdP"Y8  88      88      88  88  
                                                     
''')

#Verificação do SO
so = platform.system()

#Verificação do IP
myip = socket.gethostbyname(socket.gethostname())

if so == 'Windows':
    print('=-' * 50)
    print("SO: Windows")
    print('HostName:', platform.node())
    #Arquiterura do processador
    #print('Processador:', platform.machine())
    print('Version:', platform.platform())
    print('Adictional Inf:', platform.win32_ver())
    print('Host-IP:', myip)
    print('=-' *50)

    #Portas OPEN
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target = myip
    print('Target ', target)

    def pscan(port):
        try:
            s.connect((target, port))
            return True
        except:
            return None

    for x in range(0, 65536):
        if pscan(x):
            print('Port', x, 'is open')
        #else:
        #    print('Port', x, 'Closed')
    print('=-' * 50)

    #Script Import
    # Notting work
    ip = myip

    ports = 65000

    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.bind((ip, port))
        msg = 'hi'
        client.sendto(msg.encode(), (ip, port))
        data, address = client.recvfrom(1024)
        # print("Recebida ->", str(data))

        if data != None:
            print(int(port) + " -> Port is opened")
        else:
            print(int(port) + " -> Port is closed")

    print("Scan Finished")

    #Verificação de portas em funcionamento

elif so == 'Linux':
    print("SO: Linux")
    print('HostName:', platform.node())
    #Arquiterura do processador
    #print('Processador:', platform.machine())
    print('Version:', platform.platform())
    print('Adictional Inf: ', platform.linux_distribution())

    # Portas OPEN
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target = myip
    print('Target ', target)


    def pscan(port):
        try:
            s.connect((target, port))
            return True
        except:
            return None


    for x in range(0, 65536):
        if pscan(x):
            print('Port', x, 'is open')
        # else:
        #    print('Port', x, 'Closed')
    print('=-' * 50)

else:
    print("Desconhecido")
    print(platform.node())
    print(platform.machine())
