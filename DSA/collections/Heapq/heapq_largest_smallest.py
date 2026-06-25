import heapq
a=[20,10,25,40,30]
heapq.heapify(a)
max=heapq.nlargest(3,a)
min=heapq.nsmallest(3,a)
print("the largest ones are : ",max)
print("the smallest ones are : ",min)
