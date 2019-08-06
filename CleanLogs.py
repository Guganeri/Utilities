from time import sleep
from datetime import datetime
import os

#verification = 3600
verification = 60
while True:
    print(datetime.now())
    sleep(verification)
    try:
        os.mkdir('Teste0001')
        print('Diretorio criado com sucesso')
    except OSError:
        print(OSError)

    #print(os.listdir(os.getcwd()))
    try:
        for raiz, diretorios, arquivos in os.walk('/'):
            for arquivos in arquivos:
                if arquivos.endswith('.log'):
                    os.remove(os.path.join(raiz, arquivos))
        os.removedirs("Teste0001")
        print('Diretorio removido com sucesso !!! ')
    except OSError:
        print(OSError)

    print(os.listdir(os.getcwd()))
    #os.remove("arquivo.txt")
