class Solution:
    def isSorted(self, arr):
        n=len(arr)
        for i in range(1,n):
            if (arr[i-1]>arr[i]):
                return False
        return True


a=Solution()
abc=[1,2,3,4,5]
print(a.isSorted(abc))
        