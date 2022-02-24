class Solution(object):
    def twoSum(self, numbers, target):
        
        left=numbers[0]
        right=numbers[-1]
        i,j=0,0
        while True:
            summ=left+right
            if summ>target:
                j+=1
                right=numbers[-1-j]
            if summ<target:
                i+=1
                left=numbers[0+i]
            if summ==target:
                return[i+1,len(numbers)-j]
            
            

        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        