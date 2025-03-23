import sys
from datetime import datetime

MENU = """
############### MENU ###############

[1] Sacar
[2] Depositar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[6] Listar Usuários
[7] Listar Contas
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
lista_usuarios = []
usuarios = {}
num_contas = 0
AGENCIA = "0001"
datemask = "%d-%m-%Y %a"



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

def ver_extrato(saldo, extrato):
    print("\nExtrato - Últimas operações:\n" if extrato else "\nNão há movimentações")
    for operacao, detalhes in extrato.items():
        tipo = detalhes["Tipo"]
        numero = detalhes["Numero"]
        valor = detalhes["Valor"]
        print(f"{operacao} {tipo}-{numero}\t\tR${valor}")
    print(f"\nSaldo total:\t\t\t\tR${saldo:.2f}\n")
    retornar_menu()

def pode_realizar_transacao(transacoes_realizadas, limite_transacoes):
    if transacoes_realizadas < limite_transacoes:
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

def novo_usuario():
    new_cpf = input("Insira o seu CPF: ")
    if len(new_cpf) != 11 or not new_cpf.isdigit():
        print("Cpf inválido, retornando ao menu principal")
        return None

    if new_cpf in usuarios:
        print("CPF já cadastrado, verifique seus dados na opção '6'")
        return None

    usuarios[new_cpf] = {}
    
    new_name = input("Insira o seu nome: ")
    if new_name:
        usuarios[new_cpf]["Nome"] = new_name.strip().title()
    else:
        print("Nome inválido, retornando ao menu principal")
        return None
        
    new_address = input("Insira o seu endereço: ")
    if len(new_address) <= 100:
        usuarios[new_cpf]["Endereço"] = new_address.title()
    else:
        print("Endereço inválido, retornando ao menu principal")
        return None

    str_birthdate = input("Insira sua data de nascimento (DDMMAAAA): ")
    try: 
        convert_date = datetime.strptime(str_birthdate, "%d%m%Y")
        usuarios[new_cpf]["Data_de_Nascimento"] = convert_date.strftime(datemask)
        print("\nUsuário cadastrado com sucesso!\n\n")
        usuarios[new_cpf]["Cliente_desde"] = datetime.now().strftime(datemask)
        retornar_menu()
    except ValueError:
        print("Data inválida, retornando ao menu principal")
        usuarios[new_cpf].clear()
        return None

def nova_conta(num_contas, usuarios, agencia):
    new_acc = input("Para criar uma nova conta, insira seu CPF: \n")
    if len(new_acc) == 11 and new_acc.isdigit():
        if new_acc in usuarios:
            opt = input(f"Criar uma conta para o CPF {new_acc}? (Y/N): ")
            if opt.lower().strip() == "y":
                if "Contas" not in usuarios[new_acc]:
                    num_contas += 1
                    usuarios[new_acc]["Agência"] = AGENCIA
                    usuarios[new_acc]["Contas"] = [f"{num_contas:07d}"]
                    print(f"\nNova conta criada para o CPF {new_acc}: Agência {agencia}, Conta {num_contas:07d}")
                    return num_contas, usuarios
                else:
                    another_acc = input(f"{new_acc} já possui uma conta, criar uma nova conta para {new_acc}? (Y/N: )")
                    if another_acc.strip().lower() == "y":
                        num_contas += 1
                        usuarios[new_acc]["Contas"].append(f"{num_contas:07d}")
                        return num_contas, usuarios
                
            elif opt.lower().strip() == "n":
                retornar_menu()
            else:
                print("Valor inválido")
                return None
        else:
            print("\nUsuário não encontrado")
            retornar_menu()
            return None
    else:
        print("\nCPF inválido, retornando ao menu...")
        return None

def listar_usuarios():
    for users in usuarios.items():
        print(f"{users}\n")

def listar_contas():
    acc_search = input("Qual o seu CPF? ")
    if len(acc_search) == 11 and acc_search.isdigit():
        print(f"\nContas encontradas para o CPF: {acc_search}: \n")
        for conta in usuarios[acc_search]["Contas"]:
            if acc_search in usuarios:
                print(f"Agencia: {AGENCIA} - {conta}\n")
            else:
                print("\nNão há contas para o CPF informado, retornando ao menu principal")
                return None
    else:
        print("CPF inválido, retornando ao menu principal")
        return None

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
                resultado = saque(
                    saldo = saldo, 
                    valor_saque = valor_saque, 
                    limite_por_saque = limite_por_saque, 
                    numero_saques = numero_saques, 
                    limite_saques = LIMITE_SAQUES, 
                    transacoes_realizadas = transacoes_realizadas
                    )
                   
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
        ver_extrato(saldo, extrato=extrato)
    
    elif option == "4":
        novo_usuario()
    
    elif option == "5":
        num_contas, usuarios = nova_conta(num_contas, usuarios, AGENCIA)

    elif option == "6":
        listar_usuarios()

    elif option == "7":
        listar_contas()

    elif option == "0":
        sys.exit("Operação encerrada.")

    else:
        print("Opção Inválida...")
