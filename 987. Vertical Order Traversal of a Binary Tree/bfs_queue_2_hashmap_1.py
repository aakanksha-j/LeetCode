# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # similar to 314. Binary Tree Vertical Order Traversal
        # instead of order from left to right
        # here order is nodes sorted by their vallues

        # queue iterative bfs, 2 hashmaps for inner level elements with same col and outer for output on all levels same column
        # https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/231256/python-queue-%2B-hash-map

        # time: O(N log N) - n for iterating through nodes, nlogn for sorting
        # space: O(N) - for queue

        if not root: return []

        hashmap = defaultdict(list) # dictionary with lists as values
        queue = deque([(root, 0)])
        while queue:
            level_hashmap = defaultdict(list)
            for _ in range(len(queue)):
                node, c = queue.popleft()
                level_hashmap[c].append(node.val)
                if node.left:
                    queue.append((node.left, c - 1))
                if node.right:
                    queue.append((node.right, c + 1))
            for key in level_hashmap:
                level_hashmap[key].sort()
                hashmap[key] += level_hashmap[key]

        output = [hashmap[key] for key in sorted(hashmap)]

        return output

9 8 2022 Vertical order Traversal of a Binary Tree
