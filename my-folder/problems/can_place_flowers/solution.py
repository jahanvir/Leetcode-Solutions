class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    
        for i,planted in enumerate(flowerbed):
            if not planted and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i]=1
                n-=1
            if n<=0:
                return True
        return False




        