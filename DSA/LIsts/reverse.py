class Solution:

    def reverseArray(self, arr):
        left=0
        right=len(arr) - 1
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
a=Solution()
abc=[1,2,3,4,5]
a.reverseArray(abc)
print(abc)

