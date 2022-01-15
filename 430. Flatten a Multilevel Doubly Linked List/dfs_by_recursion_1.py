class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        if not head:
            return head

        pseudoHead = Node(None, None, head, None)
        return self.flatten_dfs(pseudoHead, head)

        # detach the pseudoHead from real head. Why?
        head.prev = None
        return head

    def flatten_dfs(self, prev, curr):
        """return the tail of flattened list"""

        if not curr:
            return prev

        # connecting child k's head to i
        curr.prev = prev
        prev.next = curr

        # store the next element j in a temporary variable
        temp = curr.next
        # store the tail of child sublist
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, temp)
