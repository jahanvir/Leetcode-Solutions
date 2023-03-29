class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sumprevs=0
        ans=0
        for s in sorted(satisfaction,reverse=True):
            sumprevs+=s
            if sumprevs <= 0:
                return ans
            ans+=sumprevs
        return ans
            
           
