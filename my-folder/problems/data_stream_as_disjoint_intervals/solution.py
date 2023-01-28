class SummaryRanges:

    def __init__(self):
        self.nums=set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)
        

    def getIntervals(self) -> List[List[int]]:
        intervals=[]
        seen=set()
        
        for n in self.nums:

            if n in seen:
                continue
            
            left=n
            while left-1 in self.nums:
                left-=1
                seen.add(left)
            
            right=n
            while right+1 in self.nums:
                right+=1
                seen.add(right)

            intervals.append([left,right])
        return sorted(intervals)


        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()