import heapq
a=[10,30,25,5,15,40]
b=[-n for n in a]
heapq.heapify(b)
print("the largest element ",-b[0])
