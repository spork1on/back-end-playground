# Métodos principais de strings em Python:
# - capitalize(): Converte o primeiro caractere em maiúscula.
# - lower(): Converte todos os caracteres para minúsculas.
# - upper(): Converte todos os caracteres para maiúsculas.
# - title(): Converte o primeiro caractere de cada palavra em maiúscula, e o resto em minusculas.
# - strip(): Remove espaços ou caracteres indesejados do início e do fim da string.
# - lstrip(): Remove espaços ou caracteres indesejados do início da string.
# - rstrip(): Remove espaços ou caracteres indesejados do final da string.
# - replace(old, new): Substitui todas as ocorrências de 'old' por 'new' na string.
# - split(delim): Divide a string em uma lista com base no delimitador 'delim' (padrão: espaços).
# - join(iterable): Junta elementos de um iterável em uma string usando o separador especificado.
# - find(sub): Retorna o índice da primeira ocorrência de 'sub' ou -1 se não for encontrado.
# - index(sub): Similar a find(), mas lança um ValueError se 'sub' não for encontrado.
# - count(sub): Conta o número de ocorrências de 'sub' na string.
# - startswith(prefix): Verifica se a string começa com 'prefix'.
# - endswith(suffix): Verifica se a string termina com 'suffix'.
# - isalpha(): Retorna True se a string contém apenas letras (e não está vazia).
# - isdigit(): Retorna True se a string contém apenas dígitos (e não está vazia).
# - isalnum(): Retorna True se a string contém apenas letras e/ou números (e não está vazia).
# - isspace(): Retorna True se a string contém apenas espaços.

#Maiusculas e Minusculas
curso = "PyThOn"
print(curso.upper())
print(curso.lower())
print(curso.title())

#Remover espaços
curso = "    Python   "
print(curso.strip()) #semelhante ao trim() do c#
print(curso.lstrip()) #remove espaços em branco da esquerda (left strip)
print(curso.rstrip()) #remove espaços em branco da direita (right strip)

#Junções e centralizacao
curso = "Python"

print(curso.center(10, "#")) #Adiciona caracteres dos lados da palavra, centralizando-a. padrao: espaços
print(".".join(curso)) #Sintaxe um pouco diferente. junta os caracteres iterando pela string e separando com o caractere escolhido
print("#".join(curso))

#Fatiamento de strings
#O fatiamento de strings é bem simples em python, basta indicar o indice.
#Parâmetros start/stop/step separados por ':'

nome = "Diego Henrique Bavutti"
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])

print(nome[:3])
print(nome[3:])

#substring
print(nome[1:3])
print(nome[:20:2])
print(nome[0:4:2])

#espelhamento
print(nome[::-1]) #sem start ':', sem stop ':', e -1 como step


#Strings de multiplas linhas ou Strings Triplas - Parâmetros no f-string """ mensagem """ ou '''mensagem'''
#no caso das strings multiplas, o python respeita os espaçamentos inseridos no texto normal
nome = "Diego"
mensagem = f"""
Olá meu nome é {nome}
    Eu estou aprendendo Python
        Esse é um teste de espaçamento
"""

print(mensagem)

#EXEMPLO DE MENU FACILITADO

print(f"""
    ********** MENU **********

      1- Depositar
      2- Sacar
      0- Sair

    **************************
  Obrigado por usar nosso sistema
""")