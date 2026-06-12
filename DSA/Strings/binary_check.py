# Return true if s is binary, else false
class Solution:
    def isBinary(self, s):
        count=0
        for i in s:
            if i=="0" or i=="1":
                count+=1
        if count==len(s):
            return True
        else:
            return False

s=Solution()
print(s.isBinary("01101110"))