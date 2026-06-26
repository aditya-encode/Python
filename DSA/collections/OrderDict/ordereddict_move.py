from collections import OrderedDict
a=OrderedDict([('a',1),('b',2),('c',3),('d',4)])
print(a)
a.move_to_end('a')
a.move_to_end('b',last=False)
print(a)