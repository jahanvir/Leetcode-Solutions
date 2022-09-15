# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,root,ans):
        if root==None:
            return
        ans.append(root.val)
        self.traverse(root.left,ans)
        self.traverse(root.right,ans)
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.traverse(root,ans)
        return ans
        
    

    
        