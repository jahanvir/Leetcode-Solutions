class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # preprocessing

        mapper=collections.defaultdict(list)
        for i,m in enumerate(manager):
            mapper[m].append(i)
        
        q=deque([(headID,0)])
        ans=0

        while q:
            m,time=q.popleft()
            ans=max(ans,time)
            for sub in mapper[m]:
                q.append((sub,time+informTime[m]))
        
        return ans