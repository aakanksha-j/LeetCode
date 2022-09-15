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
        if not root:
            return None
        queue = deque([root])
        while queue:
            print('Node:',queue[0].val)
            # creating a dummy leftmost node for the next (child) level
            dummy = None
            # while nodes exist at the same (i.e parent) level
            for _ in range(len(queue)):
                curr = queue.popleft()
                print('Curr:',curr.val)
                if dummy:
                    dummy.next = curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                dummy = curr
                print('dummy:',dummy.val)
        return root

# time complexity: O(n)
# space complexity: O(1)
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/961868/Python-O(n)-solution-explained
# https://www.youtube.com/watch?v=68RmOoq-OSs&t=56s&ab_channel=HappyCoding
