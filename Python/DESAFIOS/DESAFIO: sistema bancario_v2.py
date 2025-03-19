import sys
from datetime import datetime

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
LIMITE_TRANSACOES = 10
transacoes_realizadas = 0
extrato = {}
ultima_data = datetime.now().date()


def saque(saldo, valor_saque, limite_por_saque, numero_saques, limite_saques, transacoes_realizadas):
    data_transacao = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    if saldo >= valor_saque:
        if valor_saque <= limite_por_saque and numero_saques < limite_saques and transacoes_realizadas < LIMITE_TRANSACOES:
            saldo -= valor_saque
            numero_saques += 1
            transacoes_realizadas += 1
            extrato[f"{data_transacao}"] = {"Tipo": "Saque", "Numero": numero_saques, "Valor": f"{valor_saque:.2f}"}
            print(f"Saque realizado, seu novo saldo: R${saldo:.2f}")
            return saldo, numero_saques, transacoes_realizadas
        else:
            excedeu_limite = valor_saque > limite_por_saque
            excedeu_numero = numero_saques >= limite_saques
        
            if excedeu_limite:
                print("Operação não executada. Valor diário máximo = R$500.00")
            elif excedeu_numero:
                print(f"Número máximos de saques diários excedido. Número máximo permitido = {limite_saques}")
        return None
    else:
        print("Operação não executada. Saldo Insuficiente.")
        return None

def depositar(saldo, valor_deposito, numero_depositos, transacoes_realizadas):
    data_transacao = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    saldo += valor_deposito
    numero_depositos += 1
    transacoes_realizadas += 1
    extrato[f"{data_transacao}"] = {f"Tipo": "Deposito", "Numero": numero_depositos, "Valor": f"{valor_deposito:.2f}"}
    print(f"Deposito realizado com sucesso, seu novo saldo: R${saldo:.2f}")
    return saldo, numero_depositos, transacoes_realizadas

def pode_realizar_transacao(transacoes_realizadas, LIMITE_TRANSACOES):
    if transacoes_realizadas < LIMITE_TRANSACOES:
        return True
    else:
        print(f"Número de transações diárias excedido. Limite permitido: {LIMITE_TRANSACOES}\n")
        return False

def retornar_menu():
    opt = input("Retornar ao Menu Principal? (S/N) ").strip().lower()
    if opt == "s":
        return True
    elif opt == "n":
        sys.exit("Operação encerrada.")
    else:
        print("Opção inválida.")
        return retornar_menu()
    
while(True):
    data_atual = datetime.now().date()
    if data_atual != ultima_data:
        transacoes_realizadas = 0
        ultima_data = data_atual
    
    option = input(MENU)
   
    if option == "1":
        if pode_realizar_transacao(transacoes_realizadas, LIMITE_TRANSACOES):
            valor_s = input("\nQual o valor do saque? ")
            try: 
                valor_saque = float(valor_s)
            except ValueError:
                print("Valor inválido.")
                continue

            if valor_saque > 0:
                resultado = saque(saldo, valor_saque, limite_por_saque, numero_saques, LIMITE_SAQUES, transacoes_realizadas)
                   
                if resultado is not None:
                       saldo, numero_saques, transacoes_realizadas = resultado
                else:
                       continue
            else:
                print("Valor inválido.")
        else:
            retornar_menu()
       
    elif option == "2":
        if pode_realizar_transacao(transacoes_realizadas, LIMITE_TRANSACOES):
            valor_d = input("\nQual o valor do depósito? ")
            try:
                valor_deposito = float(valor_d)
            except ValueError:
                print("Valor inválido.")
                continue
            
            if valor_deposito > 0:
                saldo, numero_depositos, transacoes_realizadas = depositar(saldo, valor_deposito, numero_depositos, transacoes_realizadas) 
            else:
                print("Valor inválido.")
        else:
            retornar_menu()
    
    elif option == "3":
        print("\nExtrato - Últimas operações:\n" if extrato else "\nNão há movimentações")
        for operacao, detalhes in extrato.items():
            tipo = detalhes["Tipo"]
            numero = detalhes["Numero"]
            valor = detalhes["Valor"]
            print(f"{operacao} {tipo}-{numero}\t\tR${valor}")
        print(f"\nSaldo total:\t\t\t\tR${saldo:.2f}\n")
        retornar_menu()

    elif option == "0":
        sys.exit("Operação encerrada.")

    else:
        print("Opção Inválida...")
