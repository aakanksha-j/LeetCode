"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # short java solution's python version

        if not head:
            return head

        i = head
        if i:
            j = i.next

        while i:

            # i has child,
            if i.child:
                k = i.child # store child in a variable

                # connect child to i as its next pointer
                i.next = k
                k.prev = i # its a doubly linked list
                i.child = None # don't forget to remove it from child node

                # use of second pointer j to attach tail of k's sublist to i.next
                if j:
                    while k.next: # remember its k.next not k
                        k = k.next
                    k.next = j # attach tail to j
                    j.prev = k

            # go to the next element wherein i.child/j becomes i and child.next becomes j
            i = i.next # whether child is present or not, execute this part
            if i:
                j = i.next

        return head
