class animal:
    def __init__(self,name,sound,legs):
        self.name=name
        self.sound=sound
        self.legs=legs
     
    def speak(self):
        print(f"{self.name} is making {self.sound}")


class dog(animal):
    def __init__(self, name, sound, legs,breed):
        super().__init__(name, sound, legs)
        self.breed=breed
   
    def fetch(self):
        print(f"{self.name} is fetching the ball")

class cat(animal):
    def __init__(self, name, sound, legs,color):
        super().__init__(name, sound, legs)
        self.color=color
    
    def purr(self):
        print(f"{self.name} is purring")

d1=dog("tommy","bark",4,"lebrador")
print(d1.breed)
d1.fetch()

c1=cat("micky","meow",4,"white")
print(c1.color)
c1.purr()
