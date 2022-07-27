class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        add=0
        mul=1
        reminder=0
        while n:
            reminder=n%10
            n=n//10
            add+=reminder
            mul*=reminder
        return mul-add
        