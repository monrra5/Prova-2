from operacoes import Manipulacao
from validadores import *


class Pessoa():

    # Inserção de cadastros
    def cadastro():
        bd = Manipulacao()

        cpf = False

        # Looping de solicitação e validação de CPF
        while cpf == False:
            c_cpf = input('CPF: ')
            c_cpf = ''.join(c_cpf)
            validador_cpf = ValidadorCPF(c_cpf)
            if validador_cpf.validador():
                c_cpf = validador_cpf._snumeros(c_cpf)
                existe = bd.busca_cpf(c_cpf)
                if existe:
                    print("CPF já cadastrado")
                    cpf = False
                else:
                    cpf = True
            else:
                print("CPF inválido!")
                cpf = False

        nome = False

        # Looping de solicitação e validação de nome
        while nome == False:
            c_nome = input("Nome: ")
            c_nome = ''.join(c_nome).upper()
            validador_nome = ValidadorNome()
            if validador_nome.validador(c_nome):
                nome = True
            else:
                print("Nome inválido")
                nome = False

        email = False

        # Looping de solicitação e validação de e-mail
        while email == False:
            c_email = input("E-mail: ")
            c_email = ''.join(c_email).lower()
            validador_email = ValidadorEmail()
            if validador_email.validador(c_email):
                email = True
            else:
                print("E-mail inválido")
                email = False

        # inserir dados no banco
        return bd.inserir(c_cpf, c_nome, c_email)

    # Busca de cadastros
    def busca():
        bd = Manipulacao()
        resultado = False
        while resultado == False:
            busca = input("\n\nDigite algum dado do cadastro (CPF, nome ou e-mail): ")
            busca = ''.join(busca)

            # Valida se é um CPF
            validador_cpf = ValidadorCPF(busca)
            if validador_cpf.validador():
                c_cpf = validador_cpf._snumeros(busca)
                retorno = bd.busca_pessoa_cpf(c_cpf)
                if (retorno == False):
                    resultado = False
                else:
                    resultado = True
                    break

            # Valida se é um e-mail
            validador_email = ValidadorEmail()
            busca = ''.join(busca).lower()
            if validador_email.validador(busca):
                retorno = bd.busca_email(busca)
                if (retorno == False):
                    resultado = False
                else:
                    resultado = True
                    break

            # Se não for nenhuma das condições acima, será validado como nome
            else:
                validador_nome = ValidadorNome()
                busca = ''.join(busca).upper()
                validador_nome.validador(busca)
                retorno = bd.busca_nome(busca)
                if (retorno == False):
                    resultado = False
                    print("Nenhum resultado encontrado.")
                else:
                    resultado = True
                    break

    # Edição de cadastros
    def edita():
        bd = Manipulacao()
        cpf = False
        while cpf == False:
            c_cpf = input('Confirme o CPF do cadastro a ser editado: ')
            c_cpf = ''.join(c_cpf)
            validador_cpf = ValidadorCPF(c_cpf)
            if validador_cpf.validador():
                c_cpf = validador_cpf._snumeros(c_cpf)
                existe = bd.busca_cpf(c_cpf)
                if existe:
                    # Looping de solicitação e validação de nome
                    nome = False
                    while nome == False:
                        c_nome = input("Novo nome: ")
                        c_nome = ''.join(c_nome).upper()
                        validador_nome = ValidadorNome()
                        if validador_nome.validador(c_nome):
                            nome = True
                        else:
                            print("Nome inválido")
                            nome = False

                    email = False

                    # Looping de solicitação e validação de e-mail
                    while email == False:
                        c_email = input("Novo e-mail: ")
                        c_email = ''.join(c_email).lower()
                        validador_email = ValidadorEmail()
                        if validador_email.validador(c_email):
                            email = True
                        else:
                            print("E-mail inválido")
                            email = False

                    # Atualizar dados no banco
                    return bd.atualiza(c_nome, c_email, c_cpf)
                else:
                    cpf = False
            else:
                print("CPF inválido!")
                cpf = False

    # Inativação de cadastros
    def inativa():
        bd = Manipulacao()
        cpf = False
        # Looping de solicitação e validação de CPF
        while cpf == False:
            c_cpf = input('Confirme o CPF do cadastro a ser removido: ')
            c_cpf = ''.join(c_cpf)
            validador_cpf = ValidadorCPF(c_cpf)
            if validador_cpf.validador():
                c_cpf = validador_cpf._snumeros(c_cpf)
                existe = bd.busca_cpf(c_cpf)
                if existe:
                    # Inativa cadastro no Banco
                    bd.inativa(c_cpf)
                    cpf = True
            else:
                print("CPF inválido!")
                cpf = False
