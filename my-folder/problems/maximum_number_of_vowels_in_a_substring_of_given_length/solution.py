class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow=['a','e','i','o','u']
        n=len(s)  
        v=0
        
        for j in range(k):
            if s[j] in vow:
                v+=1  
        maxV=v
        for i in range(1,n-k+1):
            if s[i-1] in vow:
                v-=1
            if s[i+k-1] in vow:
                v+=1
            maxV=max(maxV,v)

        return maxV

        