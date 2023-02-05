class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        count_p=collections.Counter(p)
        #print(count_p)
        len_p=len(p)
        ans=[]
        for i in  range(len(s)-len_p+1):
            count_s=collections.Counter(s[i:i+len_p])
            #print(count_s)
            if count_s == count_p:
                ans.append(i)
        return ans
