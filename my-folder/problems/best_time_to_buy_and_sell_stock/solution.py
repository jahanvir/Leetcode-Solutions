class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #pick the element i
        #find maximum element in range i+1 to n
        #store that differnce in d
        #compare d in every itertaion and store max
        #o(n^2)
        n=len(prices)
        diff_max=0
        min_price=float("inf")
        for p in prices:
            min_price=min(min_price,p)
            diff_max=max(diff_max,p-min_price)
        return diff_max
