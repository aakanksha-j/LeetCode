# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__():
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):
            # if reached end of a branch, return False
            if not current_node:
                return False

            # if the current node is one of p or q
            mid = current_node == p or current_node == q

            # left recursion
            left = self.recurse_tree(current_node.left)

            # right recursion
            right = self.recurse_tree(current_node.right)

            # if any two of the three flags become true update answer
            if mid + left + right >= 2:
                self.ans = current_node

            # return true if either of three flags become true
            return left or right or mid

        recurse_tree(root)
        return self.ans
