#!/usr/bin/env python
import os
from datetime import date
import logging

self.homeDir = "C:/Users/gustavo.neri/Desktop/teste/"
self.logFIle=join(self.homeDir, "CleanUp/CleanUp.log")
loggger_handler = logging.FileHandler(self.logFIle, mode='a')
logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
loggger_handler.setFormatter(logger_formatter)
self.logger.addHandler(loggger_handler)
self.logger.info(_('Logger OK'))

pasta = "C:/Users/gustavo.neri/Desktop/teste/teste/"
arquivo = str('')
diretorio = os.listdir(pasta)
print("Listando Arquivos: ", os.listdir(pasta))
self.logger.info(msgIq1)
for arquivo in diretorio:
    if arquivo in diretorio:
        if arquivo != "certificados" and arquivo != "teste01":
            print('---removendo arquivo----')
            self.logger.info(msgIq1)
            os.remove('{}/{}'.format(pasta, arquivo))
            self.logger.info(msgIq1)
            print('%s removido da pasta %s' % (pasta, arquivo))
            self.logger.info(msgIq1)
    else:
        print('este arquivo nao existe')

log_file = path.join(path.dirname(path.realpath(__file__)), f"{date.today()}.txt")

### SGR CLEANUP TESTE ###