
class Solution:
    def convertToCamelCase(self, s):
        w=s.split(" ")
        n=len(w)
        for i in range(1,n):
            w[i]=w[i].title()
        e="".join(w)
        return e

a=Solution()
d=input()
print(a.convertToCamelCase(d))



