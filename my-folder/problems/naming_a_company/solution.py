class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        
        ans=0
        initGrp=[set() for i in range(26)]
        for i in ideas:
            initGrp[ord(i[0])-ord('a')].add(i[1:])
        
        for i in range(26-1):
            for j in range(i+1,26):
                common=len(initGrp[i] & initGrp[j])
                ans+= 2*(len(initGrp[i])-common)*(len(initGrp[j]) - common)
        return ans

                