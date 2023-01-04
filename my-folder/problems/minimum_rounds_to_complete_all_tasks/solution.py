import collections

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # tasks.sort()
        # count=1
        # last=tasks[0]
        # round=0
        # for i in range(1,len(tasks)):
        #     print(tasks[i])
        #     if tasks[i]==last:
        #         count+=1
        #     else:
        #         if count==1:
        #             return -1
        #         else:
        #             round+=(count+2)//3
        #             last=tasks[i]
        #             count=1
        # round+=(count+2)//3
        # return round
        cnt = collections.Counter(tasks)
        # print(cnt)
        return sum((x+2)//3 for x in cnt.values()) if 1 not in cnt.values() else -1
            

