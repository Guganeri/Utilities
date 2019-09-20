#!/bin/bash

install-azure()
{
    echo 
    nome="azure-cli"
    pacote=$(rpm -qa | grep "$nome" )      
    echo -n "Verificando se o Pacote $nome esta instalado."    
    if [ -n "$pacote" ] ;
    then echo
        echo "Pacote $nome ja instalado."        
    else echo
        echo Instalacao azure cli
            if !  rpm --import https://packages.microsoft.com/keys/microsoft.asc
            then
                    echo "Erro ao atualizar repo"
                    exit 1
            fi      
            if !  sh -c 'echo -e "[azure-cli]\nname=Azure CLI\nbaseurl=https://packages.microsoft.com/yumrepos/azure-cli\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/azure-cli.repo'
            then
                    echo "Error ao instalar chave"
                    exit 1
            fi 
            echo Instalando Azure CLI
            if ! yum install azure-cli -y $1
            then
                    echo "Nao foi possivel instalar o pacote $1"
                    exit 1
            fi
            echo "Instalacao finalizada"   
    fi        
}
bkp-start()
{    
    DIR_ORIG="/teste"
    BKP_NAME="BKP-"
    DIR_DEST="/BKPs"
    BKP_EXT=".tar.gz"
    
    tar zcf ${DIR_DEST}/${BKP_NAME}`date +%Y_%m_%d`${BKP_EXT} ${DIR_ORIG}
    
    N=`ls /BKPs | grep -i tar.gz | wc -l`
    Q=`ls -la|grep -e "^-"| wc -l`
    
    if [ $Q -gt 3 ];then
            ARQ=`ls /BKPs | grep -i tar.gz | head -n 1`
            rm $ARQ
    fi
}
upload-Backup()
{
    az login -u <usuario>  -p <password>
    #Criacao de container
    az storage container create --name mystoragecontainer
    #Criando grupo de armazenamento
    az group create \
    --name myResourceGroup \
    --location eastus
    #Criando conta de armazenamento
    az storage account create \
    --name gneriteste \
    --resource-group myResourceGroup \
    --location eastus \
    --sku Standard_LRS \
    --encryption blob
    #Upload de um bloob
    az storage blob upload \
    --container-name mystoragecontainer \
    --name blobName \
    --file ~/path/to/local/file
    #Listar arquivos do bloob
    az storage blob list \
    --container-name mystoragecontainer \
    --output table
    #Baixar arquivos do bloob
    #az storage blob download \
    #--container-name mystoragecontainer \
    #--name blobName \
    #--file ~/destination/path/for/file
    ##az group delete --name myResourceGroup
    
    #Upload mais rapido
    #azcopy \
    #--source /mnt/myfiles \
    #--destination https://mystorageaccount.blob.core.windows.net/mystoragecontainer \
    #--dest-key <storage-account-access-key> \
    #--include "myfile.txt"    
}
install-azure
upload-Backup
