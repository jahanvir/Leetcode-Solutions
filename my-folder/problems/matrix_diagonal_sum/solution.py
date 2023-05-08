class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i=0
        pj=0
        sj=len(mat)-1
        ans=0
        for c in range(len(mat)):
            ans+=mat[i][pj]
            if pj!=sj: 
                ans+=mat[i][sj]
            i+=1
            pj+=1
            sj-=1
        return ans
