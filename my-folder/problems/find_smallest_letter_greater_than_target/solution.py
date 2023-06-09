class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left=0
        right=len(letters)-1
        while left<=right:
            mid=(left+right)//2
            if letters[mid]<=target:
                left+=1
            else:
                right-=1
        if left == len(letters):
            return letters[0]
        return letters[left]
