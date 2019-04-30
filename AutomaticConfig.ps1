ipmo international #import module internacional config

#Exibindo informações sobre locaidade
Get-WinSystemLocale
#Definindo região
PS C:\>Set-WinSystemLocale -SystemLocale ja-JP




#Automatic Config 1.0
Get-Command *-Service

#Lista Serviços Rodando
get-service | where-object { $_.Status -eq "running" }

#Lista Serviço Especifico: Exemplo "aut"
get-service | where-object { $_.Name -eq "aut" }

#Iniciando Serviço
start-service aut