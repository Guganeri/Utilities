import platform

#Verificação do SO
so = platform.system()
if so == 'Windows':
    print("Windows")
    print('Nome do computador:',platform.node())
    print('Processador:',platform.machine())
    print('Versão:',platform.platform())
elif so == 'Linux':
    print("Linux")
    print('Nome do computador:',platform.node())
    print('Processador:',platform.machine())
    print('Versão:',platform.platform())
else:
    print("Desconhecido")
    print(platform.node())
    print(platform.machine())
