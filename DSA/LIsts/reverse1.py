class solution:
    def reverse_arr(self,arr):
        n=len(arr)
        for i in range(n//2):
            temp=arr[i]
            arr[i]=arr[n-i-1]
            arr[n-i-1]=temp
a=solution()
abc=[1,3,5,7,8,9]
a.reverse_arr(abc)
print(abc)