# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # preorder iterative traversal -

        # time: O(N) - since we visit each node exactly once
        # space: O(log N) - the tree is height balanced, therefore stack requires space based on height of tree

        n = len(nums)
        root = TreeNode(nums[n//2])
        stack = [(0, n - 1, root)]

        while stack:
            print(stack)
            start, end, node = stack.pop()

            if (start + end) % 2:
                mid = (start + end + 1) // 2 # always choose right node as root
            else:
                mid = (start + end) // 2

            # preorder
            node.val = nums[mid]
            if mid + 1 <= end:
                node.right = TreeNode(-1)
                stack.append((mid + 1, end, node.right))
            if start <= mid - 1:
                node.left = TreeNode(-1)
                stack.append((start, mid - 1, node.left))

        return root
