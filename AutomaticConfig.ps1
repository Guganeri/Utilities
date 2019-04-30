Import-Module International

################## DATA - HORA
## Definindo Horario padrão como o de Brasilia
tzutil /s "E. South America Standard Time"

## Definindo formato da data
$culture = Get-Culture
$culture.DateTimeFormat.ShortDatePattern = 'd/MM/yyyy'
Set-Culture $culture
Set-Culture 'pt-BR'
$culture.DateTimeFormat.ShortTimePattern = 'HH:mm'
#$culture.DateTimeFormat.ShortDatePattern =
#Configuração de Lingaguem
$currentlist = Get-WinUserLanguageList
#Forçando o uso da linguagem
Set-WinUserLanguageList pt-BR -Force

$currentlist | ForEach-Object {if(($_.LanguageTag -ne "pt-BR") -and ($_.LanguageTag -ne "pt-BR")){exit}}
#Configurações WinServer
#Exibindo informações sobre locaidade
Get-WinSystemLocale #OK
#Definindo região
Set-WinSystemLocale -SystemLocale pt-BR




################## CRIAÇÃO DO SERVIÇO
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