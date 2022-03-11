class Solution(object):
    def maxProfit(self, prices):
        big=0
        min_price=float("inf")
        for p in prices:
            min_price=min(min_price,p)
            big=max(big,p-min_price)
        return big
                
        """
        :type prices: List[int]
        :rtype: int
        """
        