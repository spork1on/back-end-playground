#polymorphism is the possibility of the function to operate differently based on the type of data it is working with.
#the method len(), for example, works differently when it has a string or a list as a parameter.

print(len("python")) #count the number of chars of the string
print(len([10, 20, 30])) # count the number of elements inside the list
print("\n")
#Polymorphism with inheritance
#its possible to modify a base class method when using it on a child class. making it fit better for that class.

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

def plano_de_voo(obj): #função polimórfica
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)
