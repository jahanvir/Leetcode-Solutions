
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxPossible= -100000
        maxEnds=0

        for n in nums:
            maxEnds+=n
            if maxPossible<maxEnds:
                maxPossible=maxEnds
            
            if maxEnds<0:
                maxEnds=0
        return maxPossible