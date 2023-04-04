class Solution:
    def partitionString(self, s: str) -> int:

        curr=''
        count=0

        for c in s:
            if c in curr:
                print(curr)
                count+=1
                curr=c
            else:
                curr+=c
        return count+1