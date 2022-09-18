# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        nodeMap={}
        n=len(inorder)
        
        if not preorder:
            return None
        
        for i in range(n):
            nodeMap[inorder[i]]=i
        
        
        def solve(preorder,inorder,start,end,nodeMap):
            
            if start>end:
                return None
            
            node=preorder[self.pindex]
            self.pindex+=1
            position=nodeMap[node]
            root=TreeNode(node)
            root.left=solve(preorder,inorder,start,position-1,nodeMap)
            root.right=solve(preorder,inorder,position+1,end,nodeMap)
            return root
            
                
            
        self.pindex=0
        return solve(preorder,inorder,0,n-1,nodeMap)
        