# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        n,curr=0,head

        while curr:
            n+=1
            curr=curr.next

        def Treefy(left:int, right:int)->TreeNode:
            if right<left: return None
            mid=left+right>>1
            node=TreeNode()
            node.left=Treefy(left,mid-1)
            node.val,curr[0]=curr[0].val,curr[0].next
            node.right=Treefy(mid+1,right)
            return node


        curr=[head]
        return Treefy(1,n)
