class student:
    name1="english"
    name2="maths"
    name3="science"
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def average(self):
        return (self.mark1+self.mark2+self.mark3)/3

s1=student("karan",94,96,98)
print(s1.average())