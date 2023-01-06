class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        #count sorting for optimization

        total=0
        m=max(costs)
        freq=[0]*(m+1)

        for c in costs:        #O(n)
            freq[c]+=1
        
        for cost,count in enumerate(freq):    #O(n)
            if not count:
                continue
            if cost>coins:
                return total

            c=min(count, coins//cost)
            coins-= cost*c
            total+=c
        return total
            
            
    
                       

        