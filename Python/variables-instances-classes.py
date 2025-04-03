class Student:
    
    school = "DIO" #class variables are the same for all objects(instances created) - changing it will affect all instances
    #it can be changed inside the obj itself with, in this case, aluno1.school = "DIO" - in this case it will change only in the scope of the instance aluno1

    def __init__(self, name, enrollment):
        self.name = name    #instance varibales are unique for each object(instance created) - changing one wont affect other instances
        self.enrollment = enrollment

    def __str__(self) -> str:
        return f"{self.name}, {self.enrollment} - {self.school}"
    
def show_values(*objs):
    for obj in objs:
        print(obj)

    
aluno1 = Student("Diego", 1) #
aluno2 = Student("Di", 2)

show_values(aluno1, aluno2)
print("\n")

aluno1.enrollment = 3
show_values(aluno1)

Student.school = "Python"

show_values(aluno1, aluno2)

