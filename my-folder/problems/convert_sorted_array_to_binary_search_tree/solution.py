# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def sab(arr):
            if not arr:
                return None
            n=len(arr)
            mid=n//2
            root=TreeNode(arr[mid])
            root.left=sab(arr[:mid])
            root.right=sab(arr[mid+1:])
            return root
        
        return sab(nums)



        
    

