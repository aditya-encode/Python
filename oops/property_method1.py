class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    @property
    def area(self):
        return self.length*self.width
    
    @property
    def perimeter(self):
        return 2*(self.length+self.width)

s1=rectangle(20,30)
s1.length=15
print(s1.area)
print(s1.perimeter) 