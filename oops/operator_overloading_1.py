class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        return (f"{self.real}i + {self.img}j")
    def add(self,num2):
        new_real=num2.real + self.real
        new_img=num2.img + self.img
        return (f"{new_real}i + {new_img}j")
c1=complex(2,3)
print(c1.show())

c2=complex(4,5)
print(c2.show())
print(c1.add(c2))
