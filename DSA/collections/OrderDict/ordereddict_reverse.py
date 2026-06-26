from collections import OrderedDict
a=OrderedDict([('a',1),('b',2),('c',3),('d',4)])
b=OrderedDict(reversed(list(a.items())))
for k,v in b.items():
    print(k,v) 