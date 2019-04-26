import platform, socket, sys

#Verificação do SO
so = platform.system()
#Verificação do IP
myip = socket.gethostbyname(socket.gethostname())

if so == 'Windows':
    print("SO: Windows")
    print('HostName:', platform.node())
    #Arquiterura do processador
    #print('Processador:', platform.machine())
    print('Version:', platform.platform())
    print('Adictional Inf:', platform.win32_ver())
    print('Host-IP:', myip)

    #Verificação de portas em funcionamento

    for ports in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #if s.connect_ex((sys.argv[1], ports)) == 0:
        #    print("Porta", ports, "Aberta")
        #    s.close()

elif so == 'Linux':
    print("SO: Linux")
    print('HostName:', platform.node())
    #Arquiterura do processador
    #print('Processador:', platform.machine())
    print('Version:', platform.platform())
    print('Adictional Inf: ', platform.linux_distribution())

    # Verificação de portas em funcionamento

    for ports in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s.connect_ex((sys.argv[1], ports)) == 0:
            print("Porta", ports, "Aberta")
            s.close()
else:
    print("Desconhecido")
    print(platform.node())
    print(platform.machine())

#Open Ports Windows SO




