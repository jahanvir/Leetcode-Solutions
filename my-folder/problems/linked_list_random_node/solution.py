# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.__head=head
        

    def getRandom(self) -> int:
        reservoir=-1
        curr,n=self.__head,0
        while curr:
            reservoir=curr.val if randint(1,n+1)==1 else reservoir
            curr,n=curr.next,n+1
        return reservoir
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()