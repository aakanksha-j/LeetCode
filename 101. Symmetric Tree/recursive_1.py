# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            outpair = self.isMirror(left.left, right.right)
            inpair = self.isMirror(left.right, right.left)
            return outpair and inpair
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            return self.isMirror(root.left, root.right)


"""Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false

Input: root = [1]
Output: true

Time and space complexity: O(n) because we traverse the entire tree once. n is the
total number of nodes in the tree. The number of recursive calls is bound by the
height of tree. In worst case, the tree is linear and height is O(n).

https://leetcode.com/problems/symmetric-tree/discuss/33050/Recursively-and-iteratively-solution-in-Python
"""

"""
    # recursive
    # time O(n)
    # space O(n), recursive stack
    
    def check_symmetry(self, node_left, node_right):
        # both are None
        if not node_left and not node_right:
            return True
        
        # one is None
        if not node_left or not node_right:
            return False
        
        # both have same value, check their child nodes
        return (node_left.val == node_right.val) and self.check_symmetry(node_left.left, node_right.right) and self.check_symmetry(node_left.right, node_right.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check_symmetry(root.left, root.right)
    
"""