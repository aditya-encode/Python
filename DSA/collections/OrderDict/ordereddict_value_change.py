from collections import OrderedDict
a=OrderedDict([("a",1),('b',2),('c',3),('d',4)])
a['b']=5
for k,v in a.items():
    print(k,v)