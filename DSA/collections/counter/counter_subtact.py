from collections import Counter
a=Counter([1,2,3,3,3,4,5,6,6,8,8])
a.subtract([1,1,1,2,3,3,5])
print(a)