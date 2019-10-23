#!/usr/bin/env python
import os
import shutil
from datetime import date

path = "C:/"
arquivo = str('')
diretorio = os.listdir(path)
datahoje = date.today()

arquivo_log = open('logsCleanUp.txt', 'a')
log_text = ''
logs = (f"\nROTINA Iniciada {datahoje}\n")
logs = str(logs)
arquivo_log.write(logs)
lista = (f"Lista de Diretorios:{os.listdir(path)}\n")
lista = str(lista)
arquivo_log.write(lista)

for caminho, pastas, arquivos in os.walk(path):
    for pasta in pastas[:]:
        if pasta in pastas != 'qqcoisa':
            try:
                if pasta != "certificados" and pasta != "plugins-empacotados":
                    rmlog = f"removendo diretorio ->{pasta} localizada em:{caminho} \n"
                    rmlog = str(rmlog)
                    arquivo_log.write(rmlog)
                    shutil.rmtree(os.path.join(caminho, pasta))
                else:
                    continue
            except ValueError:
                continue
        else:
            continue

#for arquivo in diretorio:
#    if arquivo in diretorio:
#        if arquivo != 'logs':
#            print('---removendo arquivo----')
#            os.remove('{}/{}'.format(pasta, arquivo))
#            removendo = ("%s removido da pasta %s \n" % (pasta, arquivo))
#            removendo = str(removendo)
#            arquivo_log.write(removendo)
#            print(removendo)
#        else:
#            continue
arquivo_log.close()