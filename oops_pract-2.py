#define an Employee class with attribute role ,department & salary.
# this class should have showDetails() method
#create an engineer class that inherit the properties of from employee & has an additional attributes like name and age.

class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.deparment=department
        self.salary=salary
    def showDetail(self):
        print(f"{self.role} is working at {self.deparment} department with {self.salary} salary")

class Engineer(Employee):
    def __init__(self,role,department,salary,name,age):
        super().__init__(role,department,salary)
        self.name=name
        self.age=age

e1=Engineer("programmer","IT",45000,"Aditya",23)
e1.showDetail()
print(e1.name)
print(e1.age)
print(e1.salary)

e2=Engineer("MARKETER","MBA",29000,"Het",22)
e2.showDetail()
print(e2.name)
print(e2.age)
print(e2.salary)