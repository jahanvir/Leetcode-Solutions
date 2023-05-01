class Solution:
    def average(self, salary: List[int]) -> float:
        maxSal=0
        minSal=salary[0]
        total=0
        for s in salary:
            if s>maxSal:
                maxSal=s
            if s<minSal:
                minSal=s
            total+=s
        return (total - minSal- maxSal)/(len(salary)-2)