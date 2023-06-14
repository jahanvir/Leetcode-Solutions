# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr=[]
        def preOrder(node):
            if node:
                if node.left:
                    preOrder(node.left)
                arr.append(node.val)
                if node.right:
                    preOrder(node.right)
        preOrder(root)
        ans=max(arr)
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1] < ans:
                ans=arr[i]-arr[i-1]
        return ans
            