class Solution:
    def largestVariance(self, s: str) -> int:
        def calVaiance(c1,c2):
            ans=0
            major=0
            minor=0
            prevB=False
            for c in s:
                if c!=c1 and c!=c2:
                    continue
                if c==c1:
                    major+=1
                else:
                    minor+=1
                if minor > 0:
                    ans=max(ans,major-minor)
                elif minor==0 and prevB:
                    ans=max(ans,major-1)
                if minor>major:
                    minor=0
                    major=0
                    prevB=True
            return ans
        return max(calVaiance(c1,c2) 
                    for c1 in string.ascii_lowercase 
                    for c2 in string.ascii_lowercase 
                    if c1!=c2)

