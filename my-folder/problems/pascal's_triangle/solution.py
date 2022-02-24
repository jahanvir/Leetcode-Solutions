class Solution(object):
    def generate(self, numRows):
        res=[]
        pre=[]
        pre.append(1)
        res.append(pre)
        for i in range(numRows-1):
            curr=[]
            curr.append(1)
            for j in range(len(pre)-1):
                curr.append(pre[j]+pre[j+1])
            curr.append(1)
            res.append(curr)
            pre=curr
        return res
            
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        