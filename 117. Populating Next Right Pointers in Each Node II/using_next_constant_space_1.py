"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        # new (parent) level
        while node:
            # creating a dummy leftmost node for the next (child) level
            curr = dummy = Node(0)
            # while nodes exist at the same (i.e parent) level
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            # no more nodes at this (parent) level, dropping to next (child) level
            node = dummy.next
        return root

# time complexity: O(n)
# space complexity: O(1)
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/961868/Python-O(n)-solution-explained
"""Node: 1
node.next: None
dummy.next: 2
Node: 2
Node: 3
dummy.next: 4
Node: 4
Node: 5
Node: 7
"""
