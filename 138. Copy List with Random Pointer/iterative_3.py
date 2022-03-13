"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # iterative with O(n) time complexity and O(1) space complexity
    def copyRandomList(self, head):
        if not head:
            return head
        # Step 1: Given linked list --> Weaved linked list
        # To set next pointers (None is not mentioned)
        ptr = head
        while ptr:
            node = Node(ptr.val, None, None)
            node.next = ptr.next
            ptr.next = node
            ptr = node.next # wrote ptr.next, remember next time

        # Step 2: Weaved linked list --> Fully Weaved list
        # To set random pointers (None is mentioned for ptr.random.next)
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            # if None condition is not mentioned, 'NoneType' object has no attribute 'next' error is thrown
            ptr = ptr.next.next

        # Step 3: Fully Weaved list --> Unweaved linked list
        # To separate the two lists and return the copied list
        ptr_old = head
        ptr_new = new_head = head.next
        while ptr_old:
            ptr_old.next = ptr_old.next.next
            ptr_new.next = ptr_new.next.next if ptr_new.next else None
            # C.next = C'.next = None
            ptr_old = ptr_old.next
            ptr_new = ptr_new.next

        return new_head
