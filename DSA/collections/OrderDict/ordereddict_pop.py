from collections import OrderedDict
a=OrderedDict([('a',1),('b',2),('c',3),('d',4)])
print(a)
b=a.popitem(last=True)
print(b)
print(a)
