class Solution:
    def mySqrt(self, x: int) -> int:
         
            start=0
            end=x//2
            if x==1:
                return 1
            while start<=end:
                mid=(start+end)//2
                
                if mid*mid == x:
                    return mid
                if mid*mid >=x:
                    end=mid-1
                else:
                    start=mid+1
                
            return end