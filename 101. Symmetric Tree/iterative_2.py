# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            stack = [(root.left, root.right)]
            while stack:
                left, right = stack.pop()
                if left is None and right is None:
                    continue
                if left is None or right is None:
                    return False
                if left.val == right.val:
                    stack.append((left.left, right.right))
                    stack.append((left.right, right.left))
                else:
                    return False
            return True


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
    # iterative
    # time O(n)
    # space O(n) for stack
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [(root.left, root.right)]
        while stack:
            node_left, node_right = stack.pop()
            
            # both are None
            if not node_left and not node_right:
                continue

            # one is None
            if not node_left or not node_right:
                return False

            # both have same value, check their child nodes
            if node_left.val == node_right.val:
                stack.append((node_left.left, node_right.right))
                stack.append((node_left.right, node_right.left))
            
            # both don't have same value
            else:
                return False
        
        return True
"""