# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # recursive solution

        # time: O(N) - iterate through each node exactly once
        # space: O(N) - recursive call stack

        # base case
        if root == None or root == p or root == q:
            return root

        # regenerative case
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        return root if (left and right) else (left or right)

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/152682/Python-simple-recursive-solution-with-detailed-explanation
# https://www.youtube.com/watch?v=13m9ZCB8gjw&t=570s&ab_channel=TusharRoy-CodingMadeSimple
