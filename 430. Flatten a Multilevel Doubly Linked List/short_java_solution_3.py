"""class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def __init(self):
        tail = Node(0)
    
    def flatten(self, head):
        if not head:
            return head

        head.prev = tail
        tail = head # variable to store tail of the sublist
        print(tail.val)

        nextnode = head.next # variable to store next element as head.chid wil become head.next

        head.next = self.flatten(head.child)
        head.child = None

        print(tail.val)
        tail.next = self.flatten(nextnode)

        return head
