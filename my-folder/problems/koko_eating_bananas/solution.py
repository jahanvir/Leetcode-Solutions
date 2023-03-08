class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left=ceil(sum(piles)/h)
        right=max(piles)

        def eatAll(speed):
            return sum((pile-1)//speed+1 for pile in piles)

        while left<right:
            mid=(left+right)//2
            if eatAll(mid)<=h:
                right=mid
            else:
                left=mid+1
        return left
