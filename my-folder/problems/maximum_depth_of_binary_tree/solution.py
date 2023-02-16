# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        depth=0
        q=[]

        q.append(root)
        #q.append(None)

        while q:
            nodecount=len(q)
            
            while nodecount >0:
                node=q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                
                if node.right is not None:
                    q.append(node.right)

                nodecount-=1
            depth+=1


        return depth