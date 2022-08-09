# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # leetcode solution - bfs without sorting
        # https://leetcode.com/problems/binary-tree-vertical-order-traversal/discuss/76420/Vertical-Order-in-Python

        # time: O(N) for traversing every node in tree
        # space: O(N) for dictionary and queue

        if not root: # problem mentions that input can contain 0 nodes
            return []

        queue = deque([(root, 0)])
        col_dic = defaultdict(list) # dictionary with lists as values
        min_col, max_col = 0, 0

        while queue:
            node, col = queue.popleft()

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

            min_col = min(col, min_col)
            max_col = max(col, max_col)

            col_dic[col].append(node.val)

        return [col_dic[col] for col in range(min_col, max_col + 1)]

        
