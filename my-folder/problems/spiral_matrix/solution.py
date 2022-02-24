class Solution(object):
    def spiralOrder(self, matrix):
        #no of rows
        m=len(matrix)
        
        #columns
        n=len(matrix[0])
        
        #start row
        k=0
        
        #start col
        l=0
        
        spiral=[]
        
        while k<m and l<n:
            for i in range(l,n):
                spiral.append(matrix[k][i])
            k+=1
            
            for i in range(k,m):
                spiral.append(matrix[i][n-1])
            n-=1
            
            if k<m:
                for i in range(n-1,l-1,-1):
                    spiral.append(matrix[m-1][i])
                m-=1
            if l<n:
                for i in range(m-1,k-1,-1):
                    spiral.append(matrix[i][l])
                l+=1
        return spiral
            
        
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        