# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive dfs
    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            self.dfs(root.left, level + 1, res)
            # left before right in recursion because internal stack places left
            # on top, in iteration right before left because while popping from
            # list, last element gets popped first, therefore left should be at
            # end of stack to ensure it get popped first and appended to res.
            self.dfs(root.right, level + 1, res)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res

#https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33731/Python-short-recursive-and-iterative-solutions
