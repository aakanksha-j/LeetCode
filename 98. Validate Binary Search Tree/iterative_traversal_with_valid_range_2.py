# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]

        while stack:
            node, low, high = stack.pop()

            if node.val <= low or node.val >= high:
                return False

            if node.right:
                stack.append(node.right, node.val, high)

            if node.left:
                stack.append(node.left, low, node.val)

        return validate(root)
