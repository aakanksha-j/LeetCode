# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using hash set
        seen = set()
        node = head
        while node:
            print(node.val)
            if node in seen:
                return node
            seen.add(node)
            node = node.next
        return None
