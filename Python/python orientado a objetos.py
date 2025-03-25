class bicicleta:
        def __init__(self, cor, modelo, ano, valor):
            self.cor = cor
            self.modelo = modelo
            self.ano = ano
            self.valor = valor

        def buzinar(self):
            return "plim, plim ..."

        def correr(self):
            return "Vrummmmm..."

        def parar(self ):
            return "Bicicleta parando...\n bicicleta parada!"

        #def __str__(self):
        #    return f"{self.cor} {self.modelo} {self.ano} {self.valor}"

        def __str__(self):
            return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}"

caloi = bicicleta("preta", "caloi", "1995", "2000")

print(caloi.correr()) #bicicleta.correr(caloi)
print(caloi.buzinar()) #bicicleta.buzinar(caloi)
print(caloi.parar()) #bicicleta.parar(caloi)
print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor)

print(caloi)
