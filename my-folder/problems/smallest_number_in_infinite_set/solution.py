class SmallestInfiniteSet:

    def __init__(self):

        self.nums=set(n for n in range(1,1001))
        

    def popSmallest(self) -> int:
        minNum=min(self.nums)
        self.nums.remove(minNum)
        return minNum
        

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            self.nums.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)