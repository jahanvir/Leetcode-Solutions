class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans=0
        people.sort()
        i=0
        j=len(people)-1

        while i<=j:
            remain = limit - people[j]
            j-=1
            if people[i] <= remain:
                i+=1
            ans+=1

        return ans

        