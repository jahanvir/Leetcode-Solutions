
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        if n==1:
            return n
        ans=2
        for i in range(n):
            slops=collections.defaultdict(int)
            for j in range(n):
                if j!=i:
                    s=math.atan2(points[j][1]-points[i][1],points[j][0]-points[i][0])
                    slops[s]+=1
            ans=max(ans,max(slops.values())+1)
        return ans
            

        
        