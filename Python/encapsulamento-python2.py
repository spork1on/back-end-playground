from datetime import datetime

class Person:
    def __init__(self, name, birth_date, nickname):
        self._name = name
        self._birth_date = birth_date
        self.nickname = nickname
        

    def __str__(self):
        return f"{__class__.__name__}: {[f'{chave, valor}' for chave, valor in self.__dict__.items()]}"
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        _current_year = "2025"
        return int(_current_year) - int(self._birth_date)
    
    def nick_check(self, nickname):
        if len(nickname) > 5:
            print("nickname too extense")
        else:
            print("nickname is ok")
        

person = Person("Diego", "1991", "bleft")
print(f"Nome: {person.name}\tIdade: {person.age}")
print(person)
person.nick_check(person.nickname)