#interfaces determine what a class should do, not how its done
#Abstract classes create contracts and cannot be instanced

#ABC is a module provided by python to create abstract classes. ABC stands for Absctract Base Class.

from abc import ABC
from abc import abstractmethod
class Remote_Controller(ABC): #works as a subclass of ABC. it designs a template for the subclasses. Cannot be instantiated
    #all subclasses must have all abstractmethods from the base class.
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def brand(self):
        pass

class TV_Controller(Remote_Controller):
    def ligar(self):
        print("The TV is on...")

    def desligar(self):
        print("TV off")

    @property
    def brand(self):
        return "Samsung"
    

class Air_Controller(Remote_Controller):
    def ligar(self):
        print("Air Conditioning on...")

    def desligar(self):
        print("Air Conditioning off...")

    @property
    def brand(self):
        return "LG"
    
tvcon = TV_Controller()
aircon = Air_Controller()

tvcon.ligar()
tvcon.desligar()
print(f"{tvcon.brand}\n")


aircon.ligar()
aircon.desligar()
print(aircon.brand)