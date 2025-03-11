#range(stop) -> range object
#range(start, stop[, step]) -> range object

#Com a função builtin range é possível retornar uma lista
print(list(range(11))) #lista items de 1-10

#o parâmetro final 'step' tem a função de determinar o espaço entre os numeros listados
#tabuada do 5

print(list(range(0, 51, 5)))

#ou, sem ser uma lista, se usa o for

for num in range(0, 51, 5):
    print(num, end=" ")