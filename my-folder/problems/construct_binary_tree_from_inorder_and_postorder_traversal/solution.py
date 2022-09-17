# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        n=len(postorder)
        #mapper for node to index for o(1)
        nodeMap={}
        for i in range(n):
            nodeMap[inorder[i]]=i


        
        def solve(inorder,postorder,Start,End,nodeMap):
            if Start>=End:
                if inorder==[] or Start>End:
                    return None
                
                node=postorder[self.pindex]
                self.pindex-=1
                return TreeNode(inorder[Start])
            else:
                if self.pindex>=0:
                    node=postorder[self.pindex]
                    self.pindex-=1
            
            root=TreeNode(node)
            position=nodeMap[node]
            
            root.right=solve(inorder,postorder,position+1,End,nodeMap)
            root.left=solve(inorder,postorder,Start,position-1,nodeMap)
            
            return root
        
        #solve(inorder,postorder,inorderstart,inorderend,size,nodeMap)
        self.pindex=len(postorder)-1
        root=solve(inorder,postorder,0,n-1,nodeMap)
        return root
    
        
    
