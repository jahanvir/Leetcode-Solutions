class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n=len(s)
        possible=0
        for i in range(n):
            freq={}
            currmax=0
            for j in range(i,n):
                if s[j] in freq:
                    break
                else:
                    freq[s[j]]=1
                    currmax+=1
                    possible=max(possible,currmax)
            
        return possible
                