class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        profit=0
        for i in range(1,n):
            profit+=max(prices[i]-prices[i-1],0)
        return profit
        """if n<2:
            return 0
        maxp,mins=float('-inf'),prices[0]
        for p in prices:
            maxp=max(maxp,p-mins)
            mins=min(mins,p)
        return maxp"""
        """
        :type prices: List[int]
        :rtype: int
        """
        