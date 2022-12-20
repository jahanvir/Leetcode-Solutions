class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[]
        al=[1 for i in range(0,len(rooms))]
        al[0]=0
        count=len(rooms)-1
        for x in rooms[0]:
            visited.append(x)
        while visited:
            x=visited.pop()
            if al[x]==1:
                al[x]=0
                count-=1
                for r in rooms[x]:
                    visited.append(r)
        
        if count==0:
            return True
        else:
            return False




