#The for in python works like the foreach in c# too
#In python its easy to iterate inside strings, cause it takes strings like a collection of characters, not being needed an array of chars.
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="\n")

print()
