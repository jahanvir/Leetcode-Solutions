# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode(0,head)
        first=head
        prev=dummy

        while first and first.next:
            
            second=first.next
            third=second.next

            second.next=first
            first.next=third
            prev.next=second

            prev=first
            first=third
        return dummy.next



