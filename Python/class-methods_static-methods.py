#class methods are attached to the class itself, and not to the objects (CLS) - used to create factory methods (that return instances of that class)
#static methods are also attached to the class, however they dont have an explicit arg. they cant access or modify the class - used to create utilitary functions

class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    @classmethod
    def create_since_birthdate(cls, year, month, day, name):
        age = 2025 - year
        return cls(name, age)
    
    @staticmethod
    def is_above_age(age):
        return age >= 18


#p = Person("Diego", 34)
#print(p.name, p.age)

p2 = Person.create_since_birthdate(1991, 3, 19, "Diego")
print(p2.name, p2.age)

print(Person.is_above_age(18))
print(Person.is_above_age(15))
print("\n")

print(Person.is_above_age(p2.age))