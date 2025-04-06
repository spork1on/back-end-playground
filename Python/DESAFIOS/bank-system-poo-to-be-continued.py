import sys
from abc import ABC
from datetime import datetime
from abc import abstractmethod

class Cliente:
    def __init__(self, _endereco):
        self._endereco = _endereco
        self._contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class Pessoa_Fisica(Cliente):
    def __init__(self, _cpf, _nome, _data_nascimento, _endereco):
        super().__init__(_endereco)
        self._cpf = _cpf
        self._nome = _nome
        self._data_nascimento = _data_nascimento

class Conta:
    def __init__(self, _numero, _cliente):
        self._saldo = 0
        self._numero = _numero
        self._agencia = "0001"
        self._cliente = _cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return f"{self._saldo:.2f}"

    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self.agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação negada! Saldo insuficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        
        else:
            print("\n@@@ Operação negada! O valor informado é inválido. @@@")
            return False

    def depositar(self, valor):
        saldo = self._saldo
        if valor > 0:
            saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        
        else:
            print("@@@ Operação negada! O valor informado é inválido. @@@")
            return False
        
        return True

class Conta_Corrente(Conta):
    def __init__(self, _numero, _cliente, _limite=500, _limite_saques=3):
        super().__init__(_numero, _cliente)
        self._limite = _limite
        self._limite_saques = _limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação não realizada! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação não realizada! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)
        
        return False

    def __str__(self):
        return f"""\
            Agência:\t{self._agencia}
            C/C:\t\t{self._numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
class Deposito:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            
def main():
    clientes = []
    contas = []

    MENU = """
############### MENU ###############

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[6] Listar Usuários
[7] Listar Contas
[0] Sair

####################################
"""
    while True:
        opt = input(MENU)
        try:
            option = int(opt)
        except ValueError:
            print("\n@@@ Opção inválida. @@@")

            if option == 1:
                pass

            elif option == 2:
                pass

            elif option == 3:
                pass

            elif option == 4:
                pass
            
            elif option == 5:
                pass

            elif option == 0:
                sys.exit("Operação cancelada.")

            else:
                print("Opção inválida")
                return

main()