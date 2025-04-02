
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print(self.name)
        print(self.name)
class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        self.name = name
        self.salary = salary
        self.post = post
        self.id_number = id_number
employee=Employee("Rahul",782004,25000,"HR Head")  
print("Info of Our Employee \n name:",employee.name,"\n Salary:", employee.salary,"\n Id Number",employee.id_number,"\n Post",employee.post)  