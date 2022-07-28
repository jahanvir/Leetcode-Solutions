class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapchar={}
        mapped=set()
        
        n=len(s)
        
        for i in range(n):
            if s[i] in mapchar:
                if mapchar[s[i]]!=t[i]:
                    return False
                
            else:
                if t[i] in mapped:
                    return False
        
                mapchar[s[i]]=t[i]
                mapped.add(t[i])
        return True
                
            
        
        