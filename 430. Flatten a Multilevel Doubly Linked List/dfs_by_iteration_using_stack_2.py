"""class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        # dfs by iteration using stack

        if not head:
            return head

        stack = [head]
        prev = Node(0) # in leetcode solution, pseudoHead = Node(0, None, head, None)

        # same format as binary tree preorder traversal 144 iterative solution
        while stack:
            curr = stack.pop() #pop the root node
            if curr.next: # append the right child before left
                stack.append(curr.next)
            if curr.child: # append left child to keep it on top of stack
                stack.append(curr.child)
                curr.child = None
            prev.next = curr
            curr.prev = prev
            prev = curr # similar to 206 reverse linked list iterative solution

        head.prev = None # to make sure prev pointer of head is None
        return head
