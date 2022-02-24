class Solution(object):
    def plusOne(self, digits):
        num=int("".join(str(i) for i in digits))
        num+=1
        return map(int,str(num))
        
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        