## Cleanup Rancher Hosts

Para fazer a limpeza das máquinas de um determinado environment no Rancher, execute o binário "cleanup" passando alguns argumentos, que são eles:

- Base URL do Rancher
- Access Key do Rancher
- Secret Key do Rancher
- Project ID do Rancher

O método de chamada do binário ficará nesta forma:
```console
cayohollanda@pc:~$ ./cleanup --baseUrl=http://rancher.com.br --accessKey=CHAVE-ACCESS-KEY --secretKey=CHAVE-SECRET-KEY --projectID=ID-DO-PROJETO 
```