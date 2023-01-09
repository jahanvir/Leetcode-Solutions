# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        curr=root

        while curr:
            if curr.left:
                last=curr.left
                while last.right and last.right != curr:
                    last=last.right
                
                if last.right:
                    last.right=None
                    curr=curr.right
                else:
                    last.right=curr
                    ans.append(curr.val)
                    curr=curr.left
            else:
                ans.append(curr.val)
                curr=curr.right
        return ans

                    



        