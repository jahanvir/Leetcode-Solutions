# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        mapper={}
        while headA:
            if headA in mapper:
                return headA
            else:
                mapper[headA]=1
            headA=headA.next

        while headB:
            if headB in mapper:
                return headB
            else:
                mapper[headB]=1
            headB=headB.next
        
        return None
        