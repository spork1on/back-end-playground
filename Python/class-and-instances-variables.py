class Estudante:
    escolha = "DIO" # class variable -> shared with objects 

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave, valor}' for chave, valor in self.__dict__.items()]}"

def show_name(obj):
    return print(obj.name)

diego = Estudante("Diego", "75604")
di = Estudante("Di", "7385935")

show_name(diego)
show_name(di)



