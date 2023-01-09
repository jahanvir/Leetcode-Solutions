# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans=ListNode(0)
        temp=ans
        c=0
        while l1 or l2 or c:
            l1val= l1.val if l1 else 0
            l2val= l2.val if l2 else 0
            s=l1val+l2val+c
            c=s//10
            newnode=ListNode(s%10)
            temp.next=newnode
            temp=newnode
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return ans.next