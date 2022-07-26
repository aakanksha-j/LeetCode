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

        # iterative solution using stack, parent pointer dictionary and ancestors set

        # time: O(N) - iterate through each node exactly once
        # space: O(N) - stack, parent pointer dictionary and ancestors set

        parent = {root: None}
        ancestors = set()
        stack = [root]

        while p not in parent or q not in parent: # iterate until we find both the nodes
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        while p:
            ancestors.add(p)
            p = parent[p] # key p = value of key p in parent dictionary which is ancestor

        while q not in ancestors:
            q = parent[q] # first occurrence of p's ancestor is their lowest common ancestor

        return q

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65236/JavaPython-iterative-solution
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/
