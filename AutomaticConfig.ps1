Import-Module International

function Show-Menu {
    param (
        [String]$Title = 'Menu'
    )
    cls
    Write-Host "========================= $Title ========================="

    Write-Host "1 - Para criar usuario ADM"
    Write-Host "2 - Configurar Ambiente"
    Write-Host "Q - Para Sair"
}
do {
    Show-Menu
    $input = Read-Host "Opcao: "
    switch ($input) {
        '1' {
            cls
            CriarUsuario
        } '2' {
            cls
            ConfigurarAmbiente
        }'q' {
            return
        }
    }
    Pause
}until($input -eq 'q')
function ConfigurarAmbiente {
    ################## DATA - HORA ##################
    ## Definindo Horario padrão como o de Brasilia
    tzutil /s "E. South America Standard Time"
    ## Definindo formato da data
    $culture = Get-Culture
    $culture.DateTimeFormat.ShortDatePattern = 'dd/MM/yyyy'
    Set-Culture $culture
    Set-Culture 'pt-BR'
    $culture.DateTimeFormat.ShortTimePattern = 'HH:mm'
    #$culture.DateTimeFormat.ShortDatePattern =

    #Configuração de Lingaguem
    $currentlist = Get-WinUserLanguageList
    #Forçando o uso da linguagem
    Set-WinUserLanguageList pt-BR -Force
    $currentlist | ForEach-Object { if (($_.LanguageTag -ne "pt-BR") -and ($_.LanguageTag -ne "pt-BR")) { exit } }

    #Configurações WinServer
    #Exibindo informações sobre locaidade
    Get-WinSystemLocale #OK
    #Definindo região
    Set-WinSystemLocale -SystemLocale pt-BR
    #Verificar as configura��es - Descomentar a linha
    #get-culture | Format-List -Property *    
}
function CriarUsuario {
    #Adicionar Usuario
    net user { usuario } { senhausuario } /passwordchg:yes /add
    #Permissão de Administrador
    net localgroup administrators { usuario } /add

    #Reiniciar
    shutdown /r        
}
