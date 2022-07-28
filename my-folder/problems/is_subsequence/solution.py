class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        point_s=0
        point_t=0
        while point_s<len(s) and point_t<len(t):
            if s[point_s]==t[point_t]:
                point_s+=1
                point_t+=1
            else:
                point_t+=1
        if point_s==len(s):
            return True
        else:
            return False
            
        