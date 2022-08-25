from models.cliente import Cliente
from utils.helper import formata_float_str_moeda

class Conta:
    codigo = 1000

    def __init__(self, cliente: Cliente):
        self.__numero = Conta.codigo
        self.__cliente = cliente
        self.__saldo = 0.0
        self.__limite = 100.0
        self.__saldo_total = self._calcula_saldo_total
        Conta.codigo += 1

    def __str__(self) -> str:
        return f'Número da conta: {self.numero} \nCliente: {self.cliente.nome} ' \
               f'\nSaldo Total: {formata_float_str_moeda(self.saldo_total)}'

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def limite(self) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor):
        self.__limite = valor

    @property
    def saldo_total(self) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self, valor):
        self.__saldo_total = valor

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def _calcula_saldo_total(self) -> float:
        return self.saldo + self.limite

    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com sucesso!')
        else:
            print('Erro ao efetuar o depósito. Tente novamente!')

    def sacar(self, valor: float):
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
            print('Saque efetuado com sucesso!')
        else:
            print('Saque não realizado. Tente novamente!')


    def transferir(self, destino: object, valor: float):
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo_total - valor
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + restante
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            print('Transferência realizada com sucesso!')
        else:
            print('Transferência não realizada. Tente novamente!')

