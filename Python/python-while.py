#while is used when the number of times the code will be executed is unknown
import sys
while(True):
    choose = input("[1]Sacar \n[2]Extrato \n[0]Sair\n")
    try:
        option = int(choose)
    except ValueError:
        sys.exit("Opcao invalida, saindo...")
    if option == 1:
        print("Sacando...")
    elif option == 2:
        print("Exibindo o extrato...")
    elif option == 0:
        break

print("Exit")