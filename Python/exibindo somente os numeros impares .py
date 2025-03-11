#exibindo somente os numeros impares de 0 a 100
for i in range(0, 101):
    if(i % 2 == 0):
        continue #pula a execucao
    print(i)
