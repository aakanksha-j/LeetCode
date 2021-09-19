# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generation(self, left, right, nums):
        if left <= right: # if = not written, then does not include extreme elements
            if (left + right) % 2:
                mid = (left + right + 1) // 2 # take the right element as root for even number of elements.
            else:
                mid = (left + right) // 2
            #print(left, right, mid)
            root = TreeNode(nums[mid])
            root.left = self.generation(left, mid - 1, nums)
            root.right = self.generation(mid + 1, right, nums)
            return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.generation(0, len(nums) - 1, nums)

"""Time complexity: O(n) since we visit each node exactly once.
Space complexity: O(n) for output and O(log n) for recursion stack"""
