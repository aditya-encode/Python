class Solution:
    def convertToCamelCase(self, s):
        result=[]
        camelcase=False
        for i in s:
            if i==" ":
                camelcase=True
            else:
                if camelcase==True:
                    result.append(i.upper())
                    camelcase=False
                else:
                    result.append(i)
        return "".join(result)
                
a=Solution()
b=input("input : ")
print(a.convertToCamelCase(b))