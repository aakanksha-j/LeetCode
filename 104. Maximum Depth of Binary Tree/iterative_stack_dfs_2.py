# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        res = 0
        while stack:
            node, level = stack.pop()
            if node and not node.left and not node.right:
                res = max(res, level)
            if node:
                if node.left:
                    stack.append((node.left, level + 1))
                if node.right:
                    stack.append((node.right, level + 1))
        return res

"""Used solution template from 111 min depth of binary tree iterative dfs soln
using min of res and level."""
