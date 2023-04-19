# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class T:
    def __init__(self, leftMax, rightMax, subtreeMax):
        self.leftMax = leftMax
        self.rightMax = rightMax
        self.subtreeMax = subtreeMax

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return T(-1,-1,-1)
            
            left = dfs(root.left)
            right = dfs(root.right)
            leftZigZag = left.rightMax+1
            rightZigZag = right.leftMax+1

            subtreeMax = max(leftZigZag, rightZigZag, left.subtreeMax,right.subtreeMax)
            return T(leftZigZag, rightZigZag, subtreeMax)
        return dfs(root).subtreeMax
            