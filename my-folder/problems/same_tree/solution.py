# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check(p,q):
            if p==None and q==None:
                return True
            if p==None or q==None:
                return False
            if p.val != q.val:
                return False
            return True
        
        queue=deque([(p,q),])
        while queue:
            point1, point2=queue.popleft()
            
            if not check(point1,point2):
                return False
            
            if point1:
                queue.append((point1.left,point2.left))
                queue.append((point1.right,point2.right))
        return True
            

