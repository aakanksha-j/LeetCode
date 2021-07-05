from collections import deque

# deque is useful in this scenario because popleft is faster than pop(0) and the
# length of queue is variable whereas list objects are optimized for fixed-length
# operations.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res, queue = [], deque()
        if root:
            queue.append(root)
        while queue:
            cur_level, size = [], len(queue)
            for _ in range(level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res

#https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33731/Python-short-recursive-and-iterative-solutions
