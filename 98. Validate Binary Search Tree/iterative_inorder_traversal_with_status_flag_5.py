# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = -math.inf

        stack = [(root, False)]
        while stack:
            node, status = stack.pop()

            if status is False:
                # inorder traversal
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))

            else:
                if node.val <= prev:
                    return False
                else:
                    prev = node.val

        return True


        
