"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # two pointers iteration
        # 5 cases to be handled
        # 1 before loop (no element), 3 inside loop, 1 after loop (1 element)

        # case 1: list is empty [], and we need to insert a new element
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        # case 2: value of new element lies in between the head and tail elements
        # (missed p1.val or p2.val = insertVal) here p2.val because it comes faster and saves one loop
        # case 3: value of new element is less than or equal to head element
        # case 4: value of new element is greater than or equal to tail element
        p1, p2 = head, head.next

        while True:
            if (p1.val > p2.val and (insertVal <= p2.val or insertVal >= p1.val) ) or (p1.val < insertVal <= p2.val):
                print(p1.val, p2.val)
                p1.next = Node(insertVal, p2)
                """node = Node(insertVal, p2)
                p1.next = node"""
                return head
            p1, p2 = p1.next, p2.next
            if p1 == head:
                break

        # case 5: new element was not inserted, list has one element (p1 == p2)
        p1.next = Node(insertVal, p2)
        return head
