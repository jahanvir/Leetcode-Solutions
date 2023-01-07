class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        possible=0
        ans=0
        su=0
        for i in range(len(gas)):
            possible+=gas[i]-cost[i]
            su+=gas[i]-cost[i]
            if su<0:
                su=0
                ans=i+1
        return -1 if possible<0 else ans
