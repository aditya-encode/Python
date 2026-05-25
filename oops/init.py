class Student:
    name="anonymous"
    clg_name="ganpat university"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

s1=Student("karan",95)
print(s1.name)

s2=Student("",98)
print(s2.name)
