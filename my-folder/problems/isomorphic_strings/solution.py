class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        counts={}
        countt={}
        mapper={}

        for i in range(len(s)):
            if s[i] in mapper:
                if mapper[s[i]] != t[i]:
                    return False
                counts[s[i]]+=1
                countt[t[i]]+=1
            else:
                if s[i] not in counts and t[i] not in countt:
                    counts[s[i]]=1
                    countt[t[i]]=1
                else:
                    return False
            mapper[s[i]]=t[i]


        return True