#constructor method is a method that initiates a new instance of our class. in this method, we initiate the state of our object
#to declare the constructor of a class, make use of __init__ method
#those methods __xxx__ are called special methods, and should only be used with knowledge about it

class Pet:
    def __init__(self, species, name, color, awake=True):
        self.species = species
        self.name = name
        self.color = color
        self.awake = awake
        print("Initializing class")

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{key}={value}' for key, value in self.__dict__.items()]}"

    def bark(self):
        return f'{self.name} barks!'

    def __del__(self): #destructor class method
        print("class instance deleted")

##outside methods can also create new instances of the class
def create_pet():
    luigi = Pet("cat","Luigi", "crazy gray", False)
    print("Luigi succesfully created")

filomena = Pet("dog", "Filomena", "black and yellow", True)

print(filomena.bark())
create_pet()
