# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            
            if fast==slow:
                break
        if not fast or not fast.next:
            return None
        
        slow = head

        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return fast