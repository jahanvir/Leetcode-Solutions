class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mapp=[0 for _ in range(n+1)]
        for a,b in trust:
            mapp[a]-=1
            mapp[b]+=1         
        
        for i in range(1,n+1):
            if mapp[i]==n-1:
                return i
        return -1
