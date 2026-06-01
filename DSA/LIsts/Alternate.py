class Solution:
    def get_alternat(self,arr):
        return arr[::2]
a=Solution()
abc=[1,2,3,4,5]
print(a.get_alternat(abc))