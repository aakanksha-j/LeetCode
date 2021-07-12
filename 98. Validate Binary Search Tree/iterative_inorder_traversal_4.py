# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        stack, prev = [], -math.inf
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if node.val <= prev:
                return False
            prev = node.val
            root = node.right
        return True
