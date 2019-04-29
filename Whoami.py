import platform
import socket
import sys
from pip._vendor.distlib.compat import raw_input

"""
 [] Script for devops
 [] Checking ports in use and opening ports via command line
 [] Create by: Gustavo Neri
"""
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

#Verification SO
so = platform.system()

#Verification IP
myip = socket.gethostbyname(socket.gethostname())

#Starting Utility
if so == 'Windows':
    print('=-' * 50)
    print('\n')
    print("SO: Windows")
    print('HostName:', platform.node())
    #Arquiterura do processador
    #print('Processador:', platform.machine())
    print('Version:', platform.platform())
    print('Adictional Inf:', platform.win32_ver())
    print('Host-IP:', myip)
    print('\n')
    print('=-' *50)

    #Script by pythonforbeginners Custom for Gustavo Neri

    remoteServer = raw_input("Enter a remote host to scan or you Host-Ip: ")
    remoteServerIP = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print("=-" * 50)
    print("Please wait, scanning select host", remoteServerIP)
    print("=-" * 50)

    # Check what time the scan started

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

    # We also put in some error handling for catching errors

    try:
        for port in range(1, 500):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    #Need optimized

elif so == 'Linux':
    print("SO: Linux")
    print('HostName:', platform.node())
    #Arquiterura do processador
    #print('Processador:', platform.machine())
    print('Version:', platform.platform())
    print('Adictional Inf: ', platform.linux_distribution())

    # Ports OPEN
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target = myip
    print('Target ', target)

    # Script by pythonforbeginners Custom for Gustavo Neri

    remoteServer = raw_input("Enter a remote host to scan or you Host-Ip: ")
    remoteServerIP = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print("=-" * 50)
    print("Please wait, scanning select host", remoteServerIP)
    print("=-" * 50)

    # Check what time the scan started

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

    # We also put in some error handling for catching errors

    try:
        for port in range(1, 500):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Need optimized

else:
    print("Desconhecido")
    print(platform.node())
    print(platform.machine())
