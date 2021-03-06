################## CRIAÇÃO DO SERVIÇO ##################
#Iniciando um serviço setando o caminho
Start-Process -Filepath "C:\Program Files (x86) GoogleChromeApplicationchrome.exe"

#Automatic Config 1.0
Get-Command *-Service

#Lista Serviços Rodando
get-service | where-object { $_.Status -eq "running" }

#Lista Serviço Especifico: Exemplo "aut"
get-service | where-object { $_.Name -eq "aut" }

#Iniciando Serviço
start-service aut
