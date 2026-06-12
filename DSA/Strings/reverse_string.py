#User function Template for python3

class Solution:
     def reverseString(self, s):
        k=2
        result=s[-k:]+s[:-k]
        
        return "".join(result)
    
a=Solution()
print(a.reverseString("Hello"))