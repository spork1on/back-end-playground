import sys

MENU = """
############### MENU ###############

[1] Sacar
[2] Depositar
[3] Extrato
[0] Sair

####################################
"""
saldo = 0
limite_por_saque = 500
numero_saques = 0
LIMITE_SAQUES = 3
numero_depositos = 0
extrato = {}


def saque(saldo, valor_saque, limite_por_saque, numero_saques, limite_saques):
    if saldo > valor_saque:
        if valor_saque <= limite_por_saque and numero_saques < limite_saques:
            saldo -= valor_saque
            numero_saques += 1
            extrato[f"Saque {numero_saques}"] = valor_saque
            print(f"Saque realizado, seu novo saldo: R${saldo:.2f}")
            return saldo, numero_saques
        else:
            excedeu_limite = valor_saque > limite_por_saque
            excedeu_numero = numero_saques >= limite_saques
        
            if excedeu_limite:
                print("Operação não executada. Valor diário máximo = R$500.00")
                return saldo, numero_saques

            elif excedeu_numero:
                print(f"Número máximos de saques diários excedido. Número máximo permitido = {limite_saques}")
                return saldo, numero_saques
        
            return saldo, numero_saques
    else:
        print("Operação não executada. Saldo Insuficiente.")
        return saldo, numero_saques

def depositar(saldo, valor_deposito, numero_depositos):
    saldo += valor_deposito
    numero_depositos += 1
    extrato[f"Deposito {numero_depositos}"] = valor_deposito
    print(f"Deposito realizado com sucesso, seu novo saldo: R${saldo:.2f}")
    return saldo, numero_depositos

while(True):
    option = input(MENU)
   
    if option == "1":
        valor_s = input("\nQual o valor do saque? ")
        try: 
            valor_saque = float(valor_s)
        except ValueError:
            print("Valor inválido.")
            continue

        if valor_saque > 0:
            saldo, numero_saques = saque(saldo, valor_saque, limite_por_saque, numero_saques, LIMITE_SAQUES)
        else:
            print("Valor inválido.")
    
    elif option == "2":
        valor_d = input("\nQual o valor do depósito? ")
        try:
            valor_deposito = float(valor_d)
        except ValueError:
            print("Valor inválido.")
            continue

        if valor_deposito > 0:
            saldo, numero_depositos = depositar(saldo, valor_deposito, numero_depositos)
        else:
            print("Valor inválido.")
    
    elif option == "3":
        print("\nExtrato - Últimas operações:\n" if extrato else "\nNão há movimentações")
        for chave, valor in extrato.items():
            print(f"{chave}:\tR${valor:.2f}")
        
        print(f"\nSaldo total:\tR${saldo:.2f}")

    elif option == "0":
        sys.exit("Operação encerrada.")

    else:
        print("Opção Inválida...")
