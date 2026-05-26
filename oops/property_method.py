class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        
    
    @property
    def percentage(self):
        return (self.phy+self.chem+self.math)/3

    
s1=student(95,96,97)
s1.phy=91
print(s1.phy)
print(s1.percentage)