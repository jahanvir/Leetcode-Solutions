# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def inorder(node):
            nonlocal pred,ans
            if not node:
                return

            inorder(node.left)
            if pred >=0:
                ans=min(ans, node.val - pred)
            pred=node.val
            inorder(node.right)
        
        pred=-1
        ans=100000
        inorder(root)
        return ans

       



        