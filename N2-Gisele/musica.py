import psycopg2
from Conexao import Postconexao


class ManipulacaoSQL():


    def inserir(self, nome, autor, genero):

        try:

            conexao = Postconexao().get_connection()
            cursor = conexao.cursor()

            inserir = """insert into musica (nome, autor, genero) values ('{0}','{1}','{2}')""".format(nome, autor,
                                                                                                       genero)
            cursor.execute(inserir)
            conexao.commit()
            print("Cadastro inserido com sucesso!")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)

        finally:

            if Postconexao:
                cursor.close()
                conexao.close()


persistencia = ManipulacaoSQL()

print("Tabela de Músicas \nInforme os dados abaixo solicitados:")
nome = input("Nome: ")
autor = input("Autor: ")
genero = input("Gênero: ")
persistencia.inserir(nome, autor, genero)
