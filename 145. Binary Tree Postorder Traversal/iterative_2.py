# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return res[::-1]

# Not reverse of preorder. Add root to output list. Dump left first to stack
# and then right since LIFO. Return the output in reverse order.
