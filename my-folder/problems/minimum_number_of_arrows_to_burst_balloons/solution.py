class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow=0
        latest=-float('inf')
        for p in sorted(points):
            if p[0]>latest:
                latest=p[1]
                arrow+=1
            if p[1]<latest:
                latest=p[1]
        return arrow


