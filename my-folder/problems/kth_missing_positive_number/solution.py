class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left=0
        right=len(arr) 
        
        while left<right:
            mid=(left+right)//2
            if arr[mid]-mid-1 >= k:
                right=mid
            else:
                left=mid+1
        
        return left+k