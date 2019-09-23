#!/bin/bash
export PATH=/bin:/usr/bin:/usr/local/bin

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
dump()
{
    # Update below values
    TODAY=`date +"%d%b%Y"`
    #mysqldump -u [USERNAME] -p[PASSWORD] [DATABASE-NAME] > [NOMEdoDUMP{$TODAY}].sql
    DB_BACKUP_PATH='/backup/dbbackup'
    MYSQL_HOST='localhost'
    MYSQL_PORT='3306'
    MYSQL_USER='root'
    MYSQL_PASSWORD='root'
    DATABASE_NAME='mydb'
    BACKUP_RETAIN_DAYS=30   ## Number of days to keep local backup copy

    mkdir -p ${DB_BACKUP_PATH}/${TODAY}
    echo "Backup started for database - ${DATABASE_NAME}"


    mysqldump -h ${MYSQL_HOST} \
            -P ${MYSQL_PORT} \
            -u ${MYSQL_USER} \
            -p${MYSQL_PASSWORD} \
            ${DATABASE_NAME} | gzip > ${DB_BACKUP_PATH}/${TODAY}/${DATABASE_NAME}-${TODAY}.sql.gz

    if [ $? -eq 0 ]; then
    echo "Database backup successfully completed"
    else
    echo "Error found during backup"
    exit 1
    fi
}
upload-Backup()
{    
    # Provide the name of your Storage account.
    export AZURE_STORAGE_ACCOUNT="<Storage Account Name>"

    # Provide your Storage account key.
    export AZURE_STORAGE_ACCESS_KEY="<Storage Account Key>"

    # Provide a name for your new container.
    container_name="<Container Name>"

    # Provide a name for your new blob.
    blob_name="<Blob Name>"

    # Provide the full path to a file you want to upload.
    file_to_upload="</full/path/to/file>"

    # Provide the full path to a directory you wish to use for downloaded blobs.
    destination_folder="<~/DownloadedBlobs>"

    # Upload a blob into a container
    azure storage blob upload $file_to_upload $container_name $blob_name   

    #List all blob containers
    azure storage blob list --json $container_name

    # Create a new container
    # az storage container create --name mystoragecontainer

    # Create ResourceGroup
    # az group create \
    # --name myResourceGroup \
    # --location eastus     
}