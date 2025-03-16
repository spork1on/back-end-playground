#LISTAS EM PYTHON

## CRIANDO LISTAS
#em python, tudo é objeto. as listas sao como os arrays, mas podem armazenar qualquer tipo de objeto dentro da mesma lista.
# forma mais comum de criar uma lista: []

frutas = ["laranja", "banana", "uva"]
frutas2 = [] # a lista pode ser vazia
letras = list("python") #quando se utiliza o construtor list, não se criará um objeto "python", mas sim uma sequencia de caracteres iterável.
#['p','y','t','h','o','n']
numeros = list(range(10)) #mesma lógica, mas com a função range

print(letras)
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True] #lista com valores string, int e bool na mesma lista
print(carro)

#O acesso aos dados inseridos na lista é feito por índice, começando em 0.
print(carro[0])
print(carro[2])
print(frutas[2])

##As listas também suportam indexação negativa. assim, se buscar os itens do fim para o começo da lista
print(carro[-1])
print(frutas[-1])

##As listas são também objetos e podem ser armazenadas dentro de outras listas, o que se convencionou chamar listas aninhadas ou nested lists
##as  nested lists são utilizadas principalmente para trabalhar com matrizes bidimensionais

matriz = [
    ["a", 1, 2],
    ["b", 3, 4],
    ["c", 5, 6],
]

#Nesse caso, o acesso aos dados é feito também por índice de linha x coluna
#ex:

print(matriz[0]) #primeira linha ['a', 1, 2]
print(matriz[1]) #segunda linha ['b', 3, 4]
print(matriz[0][0]) #primeira linha e primeira coluna (primeiro elemento da primeira linha) = a
print(matriz[0][-1]) #primeira linha, última coluna (último elemento da primeira linha) = 2
print(matriz[2][-1]) #terceira linha e última coluna (último elemento da terceira linha) = 6

##Fatiamento: é possivel extrair somente alguns elementos de uma sequência iterável
#ex:
#letras = ["python"]
print(letras[2:]) #iterando do índice 2 (terceira letra), até o final ':' = ['t', 'h', 'o', 'n']
print(letras[:2]) #iterando do ínício até o índice 2 = ['p', 'y']
print(letras[1:3]) #iterando do índice 1 até o indice 2 = ['y', 't']

##é possível inserir um step, ocasião em que sera iterado de acordo com o step informado
#ex:
print(letras[1:5:2]) #o terceiro argumento é o step, então será iterado de 2 em 2 = ['y', 'h']

print(letras[::]) #retorna a lista como se nao tivesse sido informado qualquer parâmetro, já que : = início, até : = fim

##Ler lista ao contrário
#em python é simples ler listas ao contrário, é só informar os parâmetros do início ao fim (::) + -1, que fará a leitura reversa

print(letras[::-1]) # ['n', 'o', 'h', 't', 'y', 'p']

##PERCORRER DADOS DE UMA LISTA.
#a forma mais comum é através do laço FOR, funcionando como um foreach de c#

for char in letras:
    print(char)

print("\n")

vehicles = ["gol", "celta", "palio"]
for car in vehicles:
    print(car)

print("\n")
##FUNÇÃO ENUMERATE
#faz a enumeração dos elementos dentro de uma lista, retornando dois valores.
for indice, carro in enumerate(vehicles):
    print(f"{indice}: {carro}")

print("\n")
##LIST COMPREHENSIONS
#utilizada para criar uma nova lista com base em elementos de uma lista predefinida
#ADICIONAR NOVOS VALORES A UMA LISTA = .APPEND()

numeros = list(range(11))
pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    
print(pares)

###COMO FAZER ISSO COM COMPREHENSION?
numeros = list(range(11))
pares = [num for num in numeros if num % 2 == 0]

print(pares)

quadrados = [quad ** 2 for quad in numeros]

print(quadrados)

print("\n\n")

###MÉTODOS DAS LISTAS EM PYTON

#APPEND() - tem a função de adicionar elementos ao final de uma lista
lista = []
lista.append(1)
lista.append("Python")
lista.append([13, 42, 54])

print(lista) #-> [1, 'Python', [13, 42, 54]]
print("\n\n")

#CLEAR() - apaga os elementos da lista
lista.clear()

print(lista)

print("\n")
#COPY() - cria uma nova instância de uma lista, evitando que seja alterada durante o código como a original

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)
print(l2)

print (id(lista)) ##não possuem o mesmo ID, o que significa que são duas instâncias diferentes da mesma lista e, alterado uma, não altera a outra.
print(id(l2))

lista.append(50)
print(lista)
print(l2)

print("\n\n")

##COUNT() - conta quantas vezes o mesmo objeto aparece dentro da lista

cores = ["vermelho", "azul", "verde", "azul"]

print(cores)
print(cores.count("azul"))
print(cores.count("vermelho"))

print("\n\n")
##EXTEND() - muito utilizado para adicionar novos elementos. Juntar uma lista com a outra. Diferete do append que só adiciona 1 elemento por vez

linguagens = ["python", "c#", "js"]
print(linguagens)

linguagens.extend(["java", "r", "rust"])
print(linguagens)

print("\n\n")

##INDEX() - passa o índice do elemento desejado. Semelhante ao IndexOf em c# (traz só a primira ocorrência, caso tenha mais de um objeto igual dentro da lista)

print(linguagens.index("java"))

print("\n\n")

##POP() - Comportamento padrão: Retira o ultimo elemento da lista. Caso passe algum indice como parâmetro, remove aquele indice.

print(linguagens)
print(linguagens.pop())
print(linguagens.pop())
print(linguagens)

print(linguagens.pop(2))
print(linguagens)

print("\n\n")

##REMOVE() - retira elementos da lista indicando o elemento propriamente.

print(linguagens)
linguagens.remove("c#")
print(linguagens)

##REVERSE() - Inverte a lista, faz o mesmo que lista[::-1]

print(frutas)

frutas.reverse()

print(frutas)

##SORT - ordena a lista. A ordem padrão é pela entrada dos dados.
#Ordenação padrão = alfabética (se a string começar com letra maiuscula, fica na frente das que começam com letra minuscula)
#Ordenação reversa = alfabética ao contrário
#Ordenção lambda = 

print(linguagens)
linguagens.extend(["c#", "c", "lua", "rust"])
print(linguagens)

linguagens.sort()
print(linguagens)

linguagens.sort(reverse=True)
print(linguagens)

print("\n")

#LAMBDA é uma função anonima que executa um código para cada item da lista

linguagens.sort(key = lambda x: len(x)) # a função lambda passará por todos os elementos da lista linguagens (x) calculando a sua extensão len(x) e reorganizando-os
#de acordo com a sua extensão
#é possivel fazer isso com reverse também
linguagens.sort(key = lambda x: len(x), reverse=True)

##LEN() - Conta quantos elementos tem na lista

print(len(linguagens)) # 6 elementos

##SORTED() - função builtin do python. serve para organizar o elementos de uma lista.

print(sorted(linguagens, key = lambda x: len(x)))   ##mesma função do sort() que é metodo das listas de python
print(sorted(linguagens, key = lambda y: len(y), reverse=True))
