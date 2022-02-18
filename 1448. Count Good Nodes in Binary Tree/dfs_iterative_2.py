# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs iterative
        stack = [(root, root.val)]
        good_nodes = 0
        while stack:
            node, max_so_far = stack.pop()
            if node:
                if node.val >= max_so_far:
                    max_so_far = node.val
                    good_nodes += 1
            if node.left:
                stack.append((node.left, max_so_far))
            if node.right:
                stack.append((node.right, max_so_far))
        return good_nodes
