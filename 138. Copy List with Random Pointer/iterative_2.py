"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visitedHash = {}

    # extra function to establish relationship
    def getClonedNode(self, head):
        if head:
            if head in self.visitedHash:
                return self.visitedHash[head]
            else:
                node = Node(head.val, None, None)
                self.visitedHash[head] = node
                return node

        return None

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # iterative with O(n) time and space complexity

        if not head:
            return head

        old_node = head
        new_node = Node(head.val, None, None)
        self.visitedHash[old_node] = new_node

        while old_node != None:
            new_node.next = self.getClonedNode(old_node.next)
            new_node.random = self.getClonedNode(old_node.random)

            old_node = old_node.next
            new_node = new_node.next

        return self.visitedHash[head]
