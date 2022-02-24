class Solution(object):
    def findDiagonalOrder(self, mat):
        
        col=len(mat)
        row=len(mat[0])
        nums=row*col
        m=n=0
        flag=True
        res=[]
        for i in range(nums):
            res.append(mat[m][n])
            if flag:
                m-=1
                n+=1
            else:
                m+=1
                n-=1
            if m>=col:
                m-=1
                n+=2
                flag=True
            elif n>=row:
                m+=2
                n-=1
                flag=False
            if m<0:
                m=0
                flag=False
            elif n<0:
                n=0
                flag=True
        return res
                
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        