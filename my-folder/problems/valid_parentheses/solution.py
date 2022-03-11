class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        openb=('(','{','[')
        closeb=(')','}',']')
        
        for i,b in enumerate(s):
            if b in openb:
                stack.append(b)
            elif not stack or openb.index(stack.pop())!=closeb.index(b):
                return False
        return not stack
                
        