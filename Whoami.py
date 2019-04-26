import platform

#Verificação do SO
so = platform.system()
if so == 'Windows':
    print("Windows")
    print('Nome do computador:',platform.node())
    print('Processador:',platform.machine())
    print('Versão:',platform.platform())
    print('#'*50)
    print('Informações adicionais SO:',platform.win32_ver())
elif so == 'Linux':
    print("Linux")
    print('Nome do computador:',platform.node())
    print('Processador:',platform.machine())
    print('Versão:',platform.platform())
    print('Distr: ',platform.linux_distribution())
else:
    print("Desconhecido")
    print(platform.node())
    print(platform.machine())
