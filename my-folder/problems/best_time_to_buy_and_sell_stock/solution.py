class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minVal=float("inf")
        maxDiff=0
        for p in prices:
            minVal=min(minVal,p)
            maxDiff=max(maxDiff,p-minVal)
        return maxDiff
        