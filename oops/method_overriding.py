class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):        # overrides parent
        print("Woof!")

class Cat(Animal):
    pass

a = Dog()
a.sound()   

b = Cat()
b.sound()  