class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=0
        prev=0
        for g in gain:
            if g+prev>ans:
                ans=g+prev
            prev=g+prev
        return ans