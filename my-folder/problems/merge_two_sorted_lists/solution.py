# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list3=None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val<list2.val:
            list3=list1
            list1=list1.next
        else:
            list3=list2
            list2=list2.next
        head=list3
        
        while list1 and list2:
            if list1.val < list2.val:
                list3.next=list1
                list1=list1.next
            else:
                list3.next=list2
                list2=list2.next
            list3=list3.next

        while list1:
            list3.next=list1
            list1=list1.next
            list3=list3.next
           
        
        while list2:
            list3.next=list2
            list2=list2.next
            list3=list3.next

        return head

