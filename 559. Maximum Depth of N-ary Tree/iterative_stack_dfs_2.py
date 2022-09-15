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
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop()
            depth = max(depth, level)
            if node:
                for child in node.children:
                    stack.append((child, level + 1))
                    # print(child.val)
        return depth

"""Iterative solution using stack and DFS. Instead of left and right nodes,
using for loop for all children. Unlike Binary tree, cannot detect if for
updating the depth, the condition if node and not node.left and not node.right,
did not check it here and updated the value of depth based on max value of level."""
