class Solution(object):
    def getRow(self, rowIndex,row=[1]):
        #row=[1]
        return self.getRow(rowIndex-1,[a+b for a,b in zip([0]+row,row+[0])]) if rowIndex else row
        
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        