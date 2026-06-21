class Solution:
    def twoSum(self, nums, target):
        for i in nums:
            b=target-i
            if b in nums:
                return (nums.index(i),nums.index(b))

a=Solution()
b=[3,4,5,6]
c=7
print(a.twoSum(b,c))


        