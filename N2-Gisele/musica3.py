from Conexao import MongoConexao
from pymongo import MongoClient
class ConexaoMongo():
    def inserir (self,nome, autor, genero):
        conexao = MongoConexao()
        inserir = {'nome': nome,'autor': autor,'genero': genero}
        conexao.connection(inserir)
        print ("Cadastro realizado com sucesso!!")


inserirmusica = ConexaoMongo()

print("Tabela de Músicas \nInforme os dados abaixo solicitados:")
nome = input("Nome: ")
autor = input("Autor: ")
genero = input("Gênero: ")
inserirmusica.inserir(nome, autor, genero)

