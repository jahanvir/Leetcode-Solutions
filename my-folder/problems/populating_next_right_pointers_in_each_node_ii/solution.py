"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        depths=[]
        nodes=[]
        
        nodes.append(root)
        depths.append(1)
        
        while nodes:
            topnode=nodes.pop(0)
            depth=depths.pop(0)
            
            if not nodes:
                topnode.next=None
            elif depths[0]>depth:
                topnode.next=None
            else:
                topnode.next=nodes[0]
            
            if topnode.left:
                nodes.append(topnode.left)
                depths.append(depth+1)
            if topnode.right:
                nodes.append(topnode.right)
                depths.append(depth+1)
        return root