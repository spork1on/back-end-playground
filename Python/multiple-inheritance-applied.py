#base class Animal. Mammal inherits from Animal and Dog, Cat, Lion inherits from both, Mammal and Animal.
#base class Animal. Bird inherits from Animal and Parrot inherits from both, Bird and Animal
class Animal:
    def __init__(self, num_paws):
        self.num_paws = num_paws

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{key}={value}' for key, value in self.__dict__.items()]}"

class Mammal(Animal):
    def __init__(self, fur_color, **kw):
        self.fur_color = fur_color
        super().__init__(**kw)

class Bird(Animal):
    def __init__(self, feather_color, beak_color, **kw):
        self.feather_color = feather_color
        self.beak_color = beak_color
        super().__init__(**kw)

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

class Lion(Mammal):
    pass

class Parrot(Bird):
    pass

Luigi = Cat("crazy-gray", num_paws=4)
Louro = Parrot("green", "black", num_paws=2)

print(Luigi)
print(Louro)