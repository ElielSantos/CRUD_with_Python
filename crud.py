#CREATE
#nome_produto = "biscoito"
#valor = 4
#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES("{nome_produto}",{valor})'
#cursor.execute(comando)
#conexao.commit() 

#READ
#comando =  f'SELECT * FROM banco1.vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall() #LER O BANCO DE DADOS
#print(resultado)

#UPDATE
#nome_produto = "halls"
#valor = 1
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() # editar banco de dados

#DELETE
#nome_produto = "biscoito"
#comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() 

# comando = ''
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados  
# resultado = cursos.fechtall() #ler o banco de dados

import mysql.connector #conexao com o MySQL

conexao = mysql.connector.connect(
    host='localhost', #your server MySQL
    user='root',      #your name user MySQL 
    password='your password',
    database='banco1', #your name database create in MySQL
)

cursor = conexao.cursor() #1 abre a conexao 

#CRUD #aqui abre os crud entre o #1 e o #2
nome_produto = "halls1"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #editar banco de dados


cursor.close() 
conexao.close() #2 fecha a conexao 



