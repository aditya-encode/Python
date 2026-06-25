import heapq
a=[20,25,10,30,40]
heapq.heapify(a)
heapq.heappush(a,5)
print(a)
b=heapq.heappop(a)
print("the smallest : ",b)
