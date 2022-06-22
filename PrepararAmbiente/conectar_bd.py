#Ativar a modulo para BD

import mysql.connector

#SETUP de configuração do BD ( usuario + senha + Url_BD)

my_connect = mysql.connector.connect(host='localhost',database='MeuDB',user='root',password='Info@1234')

if my_connect.is_connected():
    # Ver informações do servidor MySQL
    db_info = my_connect.get_server_info()
    print(f"Conectado ao servidor MYSQL versao: {db_info}")

    # enviar uma instrução para o servidor MySQL
    cursor = my_connect.cursor()
    cursor.execute("select database();")

    linha = cursor.fetchone()

    print(f"Conectado ao banco de dados: {linha}")

if my_connect.is_connected():
    cursor.close()
    my_connect.close()

    print("Conexao encerrada..!!!")
