#inheritance in POO is the resource from which a child class can receive attributes and behaviours from a father class (or base class)

class A: #class A
    pass

class B(A): #class B is a child(or a subclass) of class A
    pass

#Simple inheritance = when a class inherits attributes and behaviours from just one father class
#Multiple inheritance = when a class inherits attributes and behaviours from multiple father or base classes

class A:
    pass

class B:
    pass

class C(A, B):
    pass