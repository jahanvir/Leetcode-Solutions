class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minD=float('inf')
        index=-1
        for i in range(len(points)-1,-1,-1):
            a,b=points[i]
            if a==x or b==y:
                d=abs(a-x)+abs(b-y)
                if d<=minD:
                    minD,index=d,i
        return index
        
        