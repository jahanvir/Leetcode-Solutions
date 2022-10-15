# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        elif not list2:
            return list1
        
        out=list1
        if list1.val>list2.val:
            out=list2
            list2=list2.next
        else:
            list1=list1.next
        ph=out
        
        while list1 and list2:
            if list1.val<list2.val:
                ph.next=list1
                list1=list1.next
            else:
                ph.next=list2
                list2=list2.next
            ph=ph.next
        while list1:
            ph.next=list1
            list1=list1.next
            ph=ph.next
        while list2:
            ph.next=list2
            list2=list2.next
            ph=ph.next
        return out
        
        
            
        