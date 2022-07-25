# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # revising in bloomberg explore card, followed neetcode solution

        # time:O(N) traverse linked list
        # space: O(1) 

        # step 1: use dummy nodes to initialize
        dummy = ListNode(0, head)
        left_prev, curr = dummy, dummy.next
        # make curr reach left
        for _ in range(left - 1):
            left_prev, curr = curr, curr.next

        # step 2: reverse linked list from left to right
        prev = None
        for _ in range(right - left + 1):
            tmpNext = curr.next
            curr.next = prev
            prev, curr = curr, tmpNext

        # step 3: connect edge nodes with reversed elements
        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next
