# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        indexMap={val:i for i, val in enumerate(inorder)}

        def build(inStart,inEnd,postStart,postEnd):

            if inStart>inEnd:
                return None
                
            rootVal=postorder[postEnd]
            rootValIndex=indexMap[rootVal]
            leftSize=rootValIndex-inStart

            root=TreeNode(rootVal)
            root.left=build(inStart,rootValIndex-1,postStart,postStart+leftSize-1)
            root.right=build(rootValIndex+1,inEnd,postStart+leftSize,postEnd-1)
            return root

        return build(0,len(inorder)-1,0,len(postorder)-1)
