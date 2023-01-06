class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        number=None
        for n in nums:
            if count==0:
                number=n
            count+=(1 if n==number else -1)
        return number
            
        