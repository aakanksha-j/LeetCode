# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """ @param root, a TreeNode
            @param targetSum, an integer
            return a boolean
        """
        # base cases
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        # loop cases
        return self.hasPathSum(root.left, targetSum-root.val) or \
               self.hasPathSum(root.right, targetSum-root.val)
