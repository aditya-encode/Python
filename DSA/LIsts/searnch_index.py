class solution:
    def srch(self,arr,x):
        if x in arr:
            return arr.index(x)
        else:
            return -1
        
a=solution()
b=[1,2,3,4,5]
print(a.srch(b,10))