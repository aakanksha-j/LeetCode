# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # one pass algorithm using dummy

        # define dummy node at beginning and initialize both pointers with dummy
        dummy = ListNode()
        dummy.next = head
        first, second = dummy, dummy

        # move first pointer for n steps to maintain the gap
        for i in range(n):
            first = first.next

        # move both pointers until first reaches end
        while first.next:
            first, second = first.next, second.next

        # move second pointer
        second.next = second.next.next
        return dummy.next
