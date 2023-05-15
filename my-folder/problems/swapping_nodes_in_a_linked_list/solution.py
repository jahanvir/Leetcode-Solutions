# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        l=0
        clone=head
        headK=head
        tailK=head
        while l<k-1:
            l+=1
            clone=clone.next
        
        headK=clone
        print(headK.val)
        while clone.next:
            clone=clone.next
            tailK=tailK.next
        
        tailK.val, headK.val=headK.val,tailK.val

        return head

            
        
