class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0=coordinates[0][0]
        x1=coordinates[1][0]
        y0=coordinates[0][1]
        y1=coordinates[1][1]
        dx=x1-x0
        dy=y1-y0
        return all((x-x0)*dy == (y-y0)*dx for x,y in coordinates)
        