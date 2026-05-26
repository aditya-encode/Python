class car:
    def __init__(self,type):
        self.type="patrol"
        self.warranty="95 years"
        self.price="95 lakh"
        self.color="yellow"
        self.door=5

    @staticmethod
    def start():
        print("car started ")
        return  ""
    
    @staticmethod
    def stop():
        print("car stoped ")
        return  ""

class toyota_car(car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        self.type=type


c1=toyota_car("prius","electric")
print(c1.type)

c2=toyota_car("prius","water")
print(c2.type)
print(c2.warranty)
print(c2.price)
print(c2.color)
print(c2.door)