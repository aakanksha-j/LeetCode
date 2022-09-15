# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        ptr_in  = len(inorder) - 1
        ptr_post = len(postorder) - 2
        root = TreeNode(postorder[-1])
        stack = []
        stack.append(root)

        while ptr_post >= 0:
            curr = TreeNode(postorder[ptr_post])
            ptr_post -= 1
            prev = None

            while stack and stack[-1].val == inorder[ptr_in]:
                prev = stack.pop()
                ptr_in -= 1

            if prev:
                prev.left = curr
            else:
                stack[-1].right = curr

            stack.append(curr)

        return root

"""https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/34807/Java-iterative-solution-with-explanation
"""
