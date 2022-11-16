from conta import Conta

class Pessoafisica(Conta):
    
    __segundo_titular = ""

    def __init__(self, titular, cpf, saldo_inicial):
        super().__init__("500", "pessoafisica")
        self.__titular = titular
        self.__cpf = cpf
        self.__saldo_inicial = saldo_inicial

    @property 
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    def __str__(self):
        return f"{super().__str__()}\nTitular:> {self.__titular}\nCpf:> {self.__cpf}\nSaldo Inicial:> {self.__saldo_inicial}\nSegundo Titular:> {self.__segundo_titular}"