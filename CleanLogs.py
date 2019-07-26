from time import sleep
from datetime import datetime
import os

verification = 3600

while True:
    print (f ,' Ultima verificação em: {datetime.now()}')
    sleep(verification)
    try:
        os.mkdir('Teste0001')
        print('Diretorio criado com sucesso')
    except OSError:
        print('Diretorio não criado')
    print(os.listdir(os.getcwd()))
    os.removedirs("Teste0001")
    print(os.listdir(os.getcwd()))
    #os.remove("arquivo.txt")
