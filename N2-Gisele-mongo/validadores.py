#Importação da biblioteca re para utilizar expressões regulares para validação de e-mail e CPF
import re


#Validador de CPF
class ValidadorCPF():

    def init(self, cpf):
        self.cpf = cpf

    def validador(self):
        if not self.cpf:
            return False

        aux_validador = self._qntd_numeros(self.cpf[:9])
        aux_validador = self._qntd_numeros(aux_validador)

        if aux_validador == self.cpf:
            return True
        return False

    #Metodos para garantir um CPF válido
    @staticmethod
    def _qntd_numeros(nove):
        if not nove:
            return False

        sequencia = nove[0] * len(nove)
        if sequencia == nove:
            return False

        soma = 0
        for chave, multiplicador in enumerate(range(len(nove)+1, 1, -1)):
            soma += int(nove[chave])*multiplicador
        rd = 11 - (soma%11)
        rd = rd if rd <= 9 else 0
        return nove + str(rd)

    #Metodos para armazenar somente números
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = self._snumeros(cpf)

    @staticmethod
    def snumeros(cpf):
        return re.sub('[^0-9]', '', cpf)

#Validador de e-mail
class ValidadorEmail():

    @staticmethod
    def validador(email):
        return re.search(r"(^[a-zA-Z0-9.+-]+@[a-zA-Z0-9]+.[a-zA-Z0-9.].*[com|org|edu]{3}$)",email)

#Validador de nome
class ValidadorNome():

    @staticmethod
    def validador(nome):
        if (len(nome) < 3 or len(nome) > 150):
            return False
        return True