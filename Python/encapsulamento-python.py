class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave, valor}' for chave, valor in self.__dict__.items()]}"

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta(100)
conta.depositar(100)

#print(conta._saldo) #INCORRETO, MÁ PRÁTICA

conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())

print(conta)
print ("\n\n")
################################################################################
#PROPERTIES

class Foo:
    def __init__(self, x=None):
        self._x = x

    def __str__(self):
        return f"{__class__.__name__}: {[f'{chave, valor}' for chave, valor in self.__dict__.items()]}"

    @property #usar o @property permite que acesse o método diretamente com a sintaxe de atributo
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x += value
    
    @x.deleter
    def x(self):
        self.x = 0
    
foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)



# foo.x = 10 -> não é possivel setar o valor de x sem um property setter

