import platform, socket, sys


#Verificação do SO
so = platform.system()
if so == 'Windows':
    print("Windows")
    print('Nome do computador:', platform.node())
    print('Processador:', platform.machine())
    print('Versão:', platform.platform())
    print('#'*50)
    print('Informações adicionais SO:', platform.win32_ver())
    for ports in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #if s.connect_ex((sys.argv[1], ports)) == 0:
        #    print("Porta", ports, "Aberta")
        #    s.close()

elif so == 'Linux':
    print("Linux")
    print('Nome do computador:', platform.node())
    print('Processador:', platform.machine())
    print('Versão:', platform.platform())
    print('Distr: ', platform.linux_distribution())
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




