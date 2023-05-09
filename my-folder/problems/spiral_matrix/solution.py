class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows=len(matrix)
        cols=len(matrix[0])

        r1=0
        r2=rows-1

        c1=0
        c2=cols-1

        ans=[]

        while len(ans)< rows * cols:
            j=c1
            while j<=c2 and len(ans)<rows*cols:
                ans.append(matrix[r1][j])
                j+=1

            i=r1+1
            while i<=r2-1 and len(ans)<rows*cols:
                ans.append(matrix[i][c2])
                i+=1
            
            j=c2
            while j>=c1 and len(ans)<rows*cols:
                ans.append(matrix[r2][j])
                j-=1
            
            i=r2-1
            while i>=r1+1 and len(ans)<rows*cols:
                ans.append(matrix[i][c1])
                i-=1
            
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        return ans
            
