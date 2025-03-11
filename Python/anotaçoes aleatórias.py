import sys
valor = input("Qual o valor do depósito? ")

def depositar(valor:float):
    try: 
        amount = int(valor)
    except ValueError:
            sys.exit("Valor inválido")
    saldo = 500
    saldo += amount
    print(f"Valor depositado, seu novo saldo: {float(saldo)}")

depositar(valor)