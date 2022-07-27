# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # leetcode solution - iterative O(1) solution

        # time: O(N)
        # space: O(1)

        if not root:
            return None

        node = root
        while node:
            if node.left:
                rightmost = node.left # move to the rightmost node
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = node.right # rewire the connections
                node.right = node.left
                node.left = None
            node = node.right
