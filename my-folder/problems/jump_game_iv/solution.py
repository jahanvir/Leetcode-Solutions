class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        if n==1: return 0

        visited=set([0])
        queue=collections.deque([0])
        pos=collections.defaultdict(set)
        for i,num in enumerate(arr):
            pos[num].add(i)
        jumps=0

        while len(queue)>0:
            for _ in range(len(queue)):
                node=queue.popleft()
                if node==n-1:
                    return jumps
                nextpos=[node-1,node+1]+list(pos[arr[node]])
                for i in nextpos:
                    if 0<=i<n and i not in visited:
                        queue.append(i)
                        visited.add(i)
                pos[arr[node]]=set()
            jumps+=1
        return -1