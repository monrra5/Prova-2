from Conexao import postconexao

c = postconexao ()
nome = str(input("Digite um nome"))
c.inserir(nome)