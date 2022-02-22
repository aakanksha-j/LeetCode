# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # one pass algorithm without dummy

        if not head: return head

        first, second = head, head

        # move first pointer for n steps to maintain the gap
        for i in range(n):
            first = first.next

        # if first pointer reached end, that means first element needs to be removed
        # because for n=3, [1,2,3], 1 needs to be removed
        if not first:
            return head.next

        # move both pointers until first reaches end
        while first.next:
            first, second = first.next, second.next

        # move second pointer to skip nth node
        second.next = second.next.next
        return head
