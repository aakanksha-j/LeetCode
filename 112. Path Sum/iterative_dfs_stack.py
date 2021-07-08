# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # dfs with stack
        if not root: # input = [] will show error that stack is called before assignment.
            return False # therefore, handle that edge case here.
        stack = [(root, root.val)]
        while stack:
            node, curr_sum = stack.pop()
            #print(node.val, curr_sum)
            if not node.right and not node.left and curr_sum == targetSum:
                return True # donot return in False scenario, only true when condition is met. 
            if node.right:
                stack.append((node.right, curr_sum + node.right.val))
            if node.left:
                stack.append((node.left, curr_sum + node.left.val))
        return False

"""
input =
[5,4,8,11,null,13,4,7,2,null,null,null,1]
22
(node.val, curr_sum) =
5 5
4 9
11 20
7 27
2 22
"""
