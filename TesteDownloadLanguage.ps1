######## Download de pt-BR Teste via powershell ############
$url = "https://www.microsoft.com/pt-br/download/confirmation.aspx?id=9490"
$output = "C:\Users\gustavo.silva.ext\Desktop\Utilities"
$start_time = Get-Date

Invoke-WebRequest -Uri $url -OutFile $output
Write-Output "Time taken: $((Get-Date).Subtract($start_time).Seconds) second(s)"