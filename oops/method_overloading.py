class calculator:
    def add(self,a,b,*args):
        return a+b+sum(args)

calc=calculator()
print(calc.add(2,2))