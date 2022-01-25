# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # floyd's cycle hare and tortoise two pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = head
                while slow != slow2:
                    slow2 = slow2.next
                    slow = slow.next
                return slow
        return None

"""https://leetcode.com/problems/linked-list-cycle-ii/discuss/495311/JavaScript-Two-Pointers-w-Extended-Notes"""
