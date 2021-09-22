# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _reverse(self, node, prev = None):
        # recursive solution
        if not node:
            return prev # reached the end of [1,2,3,4,5]. prev is 5, node is null
        n = node.next # for node 2, node.next is 3
        node.next = prev # for node 2, prev is 1.
        return self._reverse(n, node) # n = 3, node = 2

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverse(head) # prev is none.
