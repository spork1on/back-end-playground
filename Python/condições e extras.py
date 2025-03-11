import sys
saldo = 2000
valor = (input("Informe o valor do saque: "))

#Semelhante ao int.TryParse(), se for possível converter, o valor é atribuído a sauqe, caso contrário, executa a exception com ValueError
try:
    saque = int(valor)
except ValueError:
    sys.exit("Opção inválida")


#IF TERNÁRIO
#if(saque is not None):
#        saldo -= saque
#        print(f"Saque efetuado, seu novo saldo é {saldo}" if saldo > saque else "Saldo insuficiente")

#status = "sucesso" if saldo > saque else "falha"
# print(status) 

#No Python não existe Null, sendo substituído por None
if saque is not None:
    if saldo > saque:
        saldo -= saque
        print(f"Saque efetuado com sucesso, seu novo saldo: {saldo}")
    else:
        print(f"Saque não executado, saldo insuficiente")
   

