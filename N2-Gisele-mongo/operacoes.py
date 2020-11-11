# Importação de biblioteca para maniplação de dados no PostgreeSQL
import psycopg2
from questao4 import Postconexao


class Manipulacao():

    # Inserção de cadastro
    def inserir(self, cpf, nome, email):
        try:
            conexao = Postconexao().get_connection()
            cursor = conexao.cursor()
            inserir = """insert into pessoas (cpf, nome, email) values ('{0}','{1}','{2}')""".format(cpf, nome, email)
            cursor.execute(inserir)
            conexao.commit()
            print("Cadastro inserido com sucesso!")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()

    # Busca por nome de cadastros ativos
    def busca_nome(self, nome):
        try:
            conexao = Postconexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where nome like '%{0}%' and status = 1".format(nome)
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            if pessoas:
                for i in pessoas:
                    print("Nome: ", i[2])
                    print("CPF: ", i[1])
                    print("E-mail: ", i[3])
                return True
            else:
                return False

        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()

    # Busca por e-mail de cadastros ativos
    def busca_email(self, email):
        try:
            conexao = Postconexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where email like '%{0}%' and status = 1".format(email)
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            for i in pessoas:
                print("Nome: ", i[2])
                print("CPF: ", i[1])
                print("E-mail: ", i[3])

        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()

    # Verificação de CPF existente no banco
    def busca_cpf(self, cpf):
        try:
            conexao = Postconexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where cpf = '{0}'".format(cpf)
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            if len(pessoas) >= 1:
                return True
            else:
                return False

        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()

    # Busca por CPF de cadastros ativos
    def busca_pessoa_cpf(self, cpf):
        try:
            conexao = Postconexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where cpf like '%{0}%' and status = 1".format(cpf)
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            if len(pessoas) >= 1:
                for i in pessoas:
                    print("Nome: ", i[2])
                    print("CPF: ", i[1])
                    print("E-mail: ", i[3])
                return True
            else:
                return False

        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()

    # Busca de todos os cadastros inativos
    def busca(self):
        try:
            conexao = Postconexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where status = 0"
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            if len(pessoas) >= 1:
                for i in pessoas:
                    print("Nome: ", i[2])
                    print("CPF: ", i[1])
                    print("E-mail: ", i[3])
                return True
            else:
                return False

        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()

    # Atualização de cadastro
    def atualiza(self, nome, email, cpf):
        try:
            conexao = Postconexao().get_connection()
            cursor = conexao.cursor()
            atualiza = "UPDATE pessoas SET nome='{0}', email='{1}' WHERE cpf = '{2}'".format(nome, email, cpf)
            cursor.execute(atualiza)
            conexao.commit()
            print("Cadastro alterado com sucesso!")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()

    # Inativação de cadastro
    def inativa(self, cpf):
        try:
            conexao = Postconexao().get_connection()
            cursor = conexao.cursor()
            atualiza = "UPDATE pessoas SET status = 0 WHERE cpf = '{0}'".format(cpf)
            cursor.execute(atualiza)
            conexao.commit()
            print("Cadastro inativado com sucesso!")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()