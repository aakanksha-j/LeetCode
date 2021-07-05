# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # using bfs with queue
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) < level + 1:
                    res.append([]) # since curr is not None, atleast one element is present.
                res[level].append(curr.val)
                queue.append((curr.left, level + 1))
                queue.append((curr.right, level + 1))
        return res

# https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/197348/Python-or-BFS-Queue-tm-(102)
# queue as a list cannot be used as when we want to access the length of treenode,
# it will not support it because treenode is not iterable.

    # using dfs with stack (append right before left)
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if curr:
                if len(res) < level + 1:
                    res.append([]) # since curr is not None, atleast one element is present.
                res[level].append(curr.val)
                if curr.right:
                    stack.append((curr.right, level + 1))
                if curr.left:
                    stack.append((curr.left, level + 1))
        return res

#https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33731/Python-short-recursive-and-iterative-solutions
