#Inheritance transfer attributes and behaviours from base to child, but also transfers its requirements and obligations.

class Vehicle:
    def __init__(self, model, color, plate, wheel_number):
        self.model = model
        self.color = color
        self.plate = plate
        self.wheel_number = wheel_number

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{key}={value}' for key, value in self.__dict__.items()]}"

    def engine_on(self):
        print(f"Turning {self.model} engine on!")

class Motorcycle(Vehicle):
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    def __init__(self, model, color, plate, wheel_number, load=False):
        super().__init__(model, color, plate, wheel_number)
        self.load = load

    def is_loaded(self): #specific method for Truck class, wont reach base classses
        print("Yes" if self.load else "No")

motorcycle = Motorcycle("daytona", "black", "abc-1234", "2")
car = Car("kicks", "pearl-white", "xxt-0098", "4")
truck = Truck("volvo", "red", "xyz-1234", "8")

motorcycle.engine_on()
print(motorcycle)
car.engine_on()
print(car)
truck.engine_on()
print(truck)
truck.is_loaded()