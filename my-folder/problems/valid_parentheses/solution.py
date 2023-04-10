class Solution:
    def isValid(self, s: str) -> bool:

        mapper = {'(':')', '[':']','{':'}'}
        keys=list(mapper.keys())
        stack=[]
        for c in s:
            if c in keys:
                stack.append(c)
            else:
                if not stack:
                    return False
                if mapper[stack.pop()] != c:
                    return False
                
        if stack:
            return False
        return True

