from collections import OrderedDict
a=OrderedDict([('a',1),('b',2),('c',3),('d',4)])
b=OrderedDict([('a',1),('b',2),('d',4),('c',3)])
print(a==b)