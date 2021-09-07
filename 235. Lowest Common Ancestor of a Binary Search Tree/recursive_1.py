# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < self.root.val and q.val < self.root.val:
            return self.lowestCommonAncestor(self.root.left, p, q)
        elif p.val > self.root.val and q.val > self.root.val:
            return self.lowestCommonAncestor(self.root.right, p, q)
        else:
            return self.root

"""https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/64980/C%2B%2B-Recursive-and-Iterative"""
