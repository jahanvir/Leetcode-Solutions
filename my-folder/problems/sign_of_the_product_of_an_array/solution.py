class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        negative=1
        for n in nums:
            if n<0:
                negative=-negative
            elif n==0:
                return 0
            
        return negative
        
            
        