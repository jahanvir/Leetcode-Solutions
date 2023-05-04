class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R,D=deque(),deque()

        for i,s in enumerate(senate):
            if s=='R':
                R.append(i)
            else:
                D.append(i)
        
        while D and R:
            dRank=D.popleft()
            rRank=R.popleft()

            if dRank<rRank:
                D.append(dRank+len(senate))
            else:
                R.append(rRank+len(senate))
        return "Radiant" if R else "Dire"