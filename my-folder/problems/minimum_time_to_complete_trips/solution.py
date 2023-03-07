class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        left=1
        right=max(time)*totalTrips

        while left<=right:
            mid=(left+right)//2

            if sum(mid//t for t in time) >= totalTrips:
                right=mid-1
            else:
                left=mid+1

        return left 