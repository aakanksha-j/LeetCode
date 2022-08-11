# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # using status flag - https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/discuss/1244022/Python-O(N)-Iterative-with-stack-Need-NOT-to-convert-to-Array
        # after 109 Convert sorted List to binary search tree

        # time: O(N)
        # space: O(N) or O(log N) - extra space for stack

        output = []

        if not root:
            return output

        stack = [(root, False)]
        while stack:
            node, status = stack.pop()

            if status is False:
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))

            else:
                output.append(node.val)

        return output
        
