class Solution(object):
    def isIsomorphic(self, s, t):
        
        
        if s==None or t==None:
            return False
        elif s=="" and t=="":
            return True
        else:
            lookup={}
            
            for i in range(len(s)):
                k=s[i]
                v=t[i]
                
                if k in lookup:
                    if lookup[k] != v:
                        return False
                else:
                    if v in lookup.values():
                        return False
                    lookup[k]=v
            return True
                    
                 
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        