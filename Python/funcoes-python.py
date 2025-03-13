#funcoes sao um bloco de codigo com um nome identificador. As funcoes aceitam parametros de entrada, que serao executados dentro da funcao.
#PARAMETROS = ENTRADA DA FUNCAO
#RETORNOS = SAIDA DA FUNCAO
#AS FUNCOES EM PYTHON SAO COMO OS METODOS EM C#

#PALAVRA RESERVADA PARA CRIACAO(DECLARAÇÃO) DE FUNCOES = 'DEF'
def exibir_mensagem():
    print("Hello World!")

def exibir_mensagem2(nome): #quando o parâmetro só esta indicado na definição da funcao, deve-se fornecer um valor para o parametro na execução da funcao
    print(f"Hello {nome}")

def exibir_mensagem3(nome="Anônimo"): #função com parâmetro padrão, caso não seha fornecido outro valor, o valor padrao (DEFAULT) nesse caso é "Anônimo"
    print(f"Hello {nome}")

exibir_mensagem()
exibir_mensagem2("Diego")
exibir_mensagem3()
exibir_mensagem3("Diego")

#Toda função retorna None por padrão, caso nao seja estipulado um return.

def calcular_total(numeros):
    return sum(numeros)

def sucessor_antecessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func3():
    print("Olá mundo")

print(calcular_total([10, 20, 34]))
print(sucessor_antecessor(10))
print(func3()) #retorna None, porque a função não possui nenhum return. Retornar None é o comportamento padrão.

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso: {marca}/{modelo}/{ano}/{placa}")

carro = {"marca": "nissan", "modelo": "kicks", "ano": "2018", "placa": "pbn4101"}

print(salvar_carro("nissan", "kicks", "2018", "pbn4101"))
print(salvar_carro(marca="nissan", modelo="kicks", ano="2018", placa="pbn4101"))
salvar_carro(**carro) #utiliando um dicionário criado anteriormente. Os caracteres ** são utilizados para desempacotar o dicionario

#É possível combinar *args e **kargs com os parametros obrigatórios das funcoes, esses que são recebidos como uma tupla e um dicionario, respectivamente.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#####*args = É usado para passar um número variável de argumentos posicionais para uma função. 
#Os argumentos são empacotados em uma tupla. Você pode usá-lo quando não sabe quantos argumentos serão passados para a função.
#O PYTHON ENTENDE COMO TUPLA VALORES SEPARADOS POR VÍRGULA E, NO EXEMPLO ABAIXO, SÓ ENTENDERÁ QUE ESTES ACABARAM QUANDO COMEÇAREM OS VALORES CHAVE=VALOR


#####**kwargs = É usado para passar um número variável de argumentos nomeados (ou seja, palavras-chave) para uma função. 
#Esses argumentos são empacotados em um dicionário.

#Em resumo: QUANDO NÃO SE SABE O NUMERO DE ARGUMENTOS

#Use *args para argumentos sem nome (posicionais) -> imprimidos no formato de tupla.

#Use **kwargs para argumentos nomeados -> imprimidos no formato de dicionário.
print("####################################################\n")

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema("Qua, 13 de mar 2025", #data_extenso
"Beautiful is better than ugly", #args
"Explicit is better than implicit", #args
"Simple is better than complex", #args
"Complex is better than complicated", #args
"Flat is better than nested", #args
"Sparse is better than dense", #args
"Readability counts", #args
"Special cases aren't special enough to break the rules", #args
"Although practicality beats purity", #args
"Errors should never pass silently", #args
"Unless explicitly silenced", #args
"In the face of ambiguity, refuse the temptation to guess", #args
"There should be one-- and preferably only one --obvious way to do it", #args
"Although that way may not be obvious at first unless you're Dutch", #args
"Now is better than never", #args
"Although never is often better than *right* now", #args
"If the implementation is hard to explain, it's a bad idea", #args
"If the implementation is easy to explain, it may be a good idea", #args
"Namespaces are one honking great idea -- let's do more of those!", #args
name="Tim Peters", year=1998) #kwargs
print("\n######################################################\n\n")


###Parâmetros especiais:
#Parâmetros posicionais: parâmetros sequenciais (colocados na posição correta na assinatura do método
#Parâmetros nomeados: são passados ao método como chave, valor (keyword)

#ORDEM DE POSICIONAMENTO DOS PARÂMETROS. A '/' e o '*' forçam a separação dos parâmetros.

#def f(pos1, pos2, / pos_or_kwd, *, kwd1, kwd2):        ##antes da barra, somente por posição
#           |             |             |               ##após a barra, por posição ou nomeado (nomeou um, pra frente serão nomeados)
#      posicionais    Pos, ou Nom     Nomeados          ##após o asterisco, somente nomeados

#POSITIONAL ONLY
def criar_carro(marca, modelo, ano, placa):
    print(marca, modelo, ano, placa)

criar_carro("nissan", "kicks", "2018", "pbn4101")

#MIXED
def criar_carro(marca, modelo, /, ano, placa): #não é obrigatório nomear após a barra, mas se ela estiver presente, antes dela deve ser obrigatoriamente por posição
    print(marca, modelo, ano, placa)

criar_carro("nissan", "kicks", ano=2018, placa="pbn4101")

#KEYWORD ONLY
def criar_carro(*, marca, modelo, ano, placa): #após o '*', somente parametros nomeados
    print(marca, modelo, ano, placa)

criar_carro(marca="nissan", modelo="kicks", ano="2018", placa="pbn4101")

print("\n#####################################\n\n")

#OBJETOS DE PRIMEIRA CLASSE:
#Em python tudo é objeto, inclusive as funções, que podem ser atribuidas a uma variável, passadas como parâmetro de outras funçoes ou usadas como valores em
#estruturas de dados (listas, tuplas, dicionarios), ou até mesmo retorno de outra função.

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(2, 5, somar)

def subtrair(a, b):
    return a - b

exibir_resultado(2, 5, subtrair)

print("\n###########################\n\n")

#Atribuição em variáveis
op = somar

print(op(1, 23))

####################################################
#Escopo Local e Global
#tudo o que ocorre dentro do escopo do método (dentro daquele bloco de código) é executado e morre com a execução do método
#Isso significa que alterações feitas em objetos imutáveis serão perdidas com a finalização do método
#para utilizar um objeto global no escopo local, utiliza-se a palavra global. Essa não é uma boa prática.

#EX:

salario = 2000

#Boa prática: a variável global é utilizada como parâmetro, mas não é alterada pelo método
def salario_bonus(salario, bonus):
    salario += bonus
    return salario

salario_bonus(salario, 500)
print(salario)

#Má prática: a variável global é utilizada diretamente no método, sendo alterada pelo seu resultado
def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(500)
print(salario)






