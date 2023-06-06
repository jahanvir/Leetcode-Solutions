class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        past=arr[0]
        diff=arr[1]-arr[0]
        for i in range(1,len(arr)):
            if arr[i]-past != diff:
                return False
            past=arr[i]
        return True