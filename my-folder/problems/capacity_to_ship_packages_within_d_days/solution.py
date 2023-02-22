class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(capacity):
            d=1
            wt=0
            for w in weights:
                wt+=w

                if wt > capacity:
                    d+=1
                    wt=w
            return d <= days

        left=max(weights)
        right=sum(weights)

        while left < right:
            mid=(left+right)//2

            if canShip(mid):
                right=mid
            else:
                left=mid+1
        return right

