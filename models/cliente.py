from datetime import date

from utils.helper import date_para_str, str_para_date

class Cliente:
    contador = 101

    def __init__(self, nome, email, cpf, data_nascimento):
        self.codigo = Cliente.contador
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__data_nascimento = str_para_date(data_nascimento)
        self.__data_cadastro = date.today()
        Cliente.contador += 1

    @property
    def data_nascimento(self) -> str:
        return date_para_str(self.__data_nascimento)

    @property
    def data_cadastro(self) -> str:
        return date_para_str(self.__data_cadastro)

    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nData nascimento: {self.data_nascimento} ' \
               f'\nData cadastro: {self.data_cadastro}'
