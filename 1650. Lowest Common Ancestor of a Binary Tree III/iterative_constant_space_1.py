"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # iterative constant space solution - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/discuss/932499/Simple-Python-Solution-with-O(1)-space-complexity

        # time: O(N)
        # space: O(1)

        left, right = p, q
        while left != right:
            left = left.parent if left.parent else q
            right = right.parent if right.parent else p
        return left
