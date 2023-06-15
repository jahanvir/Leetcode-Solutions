# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        stack=[root]
        MaxSum=root.val
        ans=1
        countLevel=0
        while stack:
            nextLevel=[]
            Lsum=0
            countLevel+=1
            for node in stack:
                Lsum+=node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if Lsum > MaxSum:
                MaxSum=Lsum
                ans=countLevel
            stack=nextLevel
        return ans
