from time import sleep
from datetime import datetime
import os

verification = 3600
#vierification = 60
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
        os.removedirs("Teste0001")
        print('Diretorio removido com sucesso !!! ')
    except OSError:
        print(OSError)

    print(os.listdir(os.getcwd()))
    #os.remove("arquivo.txt")
