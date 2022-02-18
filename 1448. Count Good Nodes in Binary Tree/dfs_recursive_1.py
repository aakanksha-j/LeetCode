# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs recursive solution
        def dfs(root, max_so_far):
            if not root:
                return 0
            good_nodes = 0
            if root.val >= max_so_far:
                max_so_far = root.val
                good_nodes += 1
            good_nodes += dfs(root.left, max_so_far)
            good_nodes += dfs(root.right, max_so_far)
            return good_nodes
        return dfs(root,root.val)
