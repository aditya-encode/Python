#most preferred answer
class Solution:
    def hasDuplicate(self, nums):
        n=len(nums)
        s=set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        
        return False
        
a=Solution()
abc=[1,2,3,3]     
print(a.hasDuplicate(abc))
