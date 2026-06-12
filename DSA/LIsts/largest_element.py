class Solution:
    def largest(self, arr):
        a=arr[0]
        b=0
        n=len(arr)
        for i in range(1,n):
            if arr[i]>a:
                a=arr[i]
        return a
er=Solution()
acd=[98,87,97,96,99,95]
print(er.largest(acd))