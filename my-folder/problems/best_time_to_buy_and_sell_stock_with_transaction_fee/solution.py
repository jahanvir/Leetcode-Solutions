class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy, sell = -prices[0],0
        
        for i in range(1, n):
            tmp=buy
            buy=max(buy,sell-prices[i])
            sell=max(sell,tmp+prices[i]-fee)
        
        return sell
