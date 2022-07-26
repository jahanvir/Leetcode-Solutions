class Solution:
    def average(self, salary: List[int]) -> float:
        maximum=0
        minimum=100000
        total=0
        n=len(salary)-2
        for s in salary:
            total+=s
            if s>maximum:
                maximum=s
            if s<minimum:
                minimum=s
        return (total-minimum-maximum)/n
            
        