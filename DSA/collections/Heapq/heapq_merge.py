import heapq
a=[20,10,25,40,30]
heapq.heapify(a)
b=[1,4,23,4,7,8,9]
c=list(heapq.merge(sorted(a),sorted(b)))
print(c)