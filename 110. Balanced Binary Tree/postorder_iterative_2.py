# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth = {None: 0}
        stack = [(0, root)]
        while stack:
            seen, node = stack.pop()
            if not node:
                continue
            if not seen:
                stack.extend([(1, node), (0, node.right), (0, node.left)])
            else:
                if abs(depth[node.left] - depth[node.right]) > 1:
                    return False
                depth[node] = max(depth[node.left], depth[node.right]) + 1
        return True
