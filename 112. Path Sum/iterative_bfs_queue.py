# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # bfs with queue
        if not root:
            return False

        queue = [(root, targetSum - root.val)]
        while queue:

            node, curr_sum = queue.pop(0)
            print(node.val, curr_sum)

            if not node.left and not node.right and curr_sum == 0:
                return True

            if node.left:
                queue.append((node.left, curr_sum - node.left.val))

            if node.right:
                queue.append((node.right, curr_sum - node.right.val))

        return False

https://leetcode.com/problems/path-sum/discuss/36486/Python-solutions-(DFS-recursively-DFS%2Bstack-BFS%2Bqueue)
