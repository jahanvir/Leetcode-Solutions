class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        n1=len(str1)
        n2=len(str2)

        def valid(index):
            if n1%index or n2%index:
                return False
            
            t1= n1//index 
            t2= n2//index

            base=str1[:index]
            return str1 == t1 * base and str2 == t2 * base

        for i in range(min(n1,n2),0,-1):
            if valid(i):
                return str1[:i]
            
        return ""


    