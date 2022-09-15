"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        queue = collections.deque([root])
        while queue:
            #print(len(queue))
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
                    # print(child.val)
        return depth

"""Iterative solution using queue and BFS. Instead of left and right nodes,
using for loop for all children."""
