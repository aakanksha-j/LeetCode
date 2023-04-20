"""
662. Maximum Width of Binary Tree
Medium
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        max_width = 1
        queue = deque([(root, 0)])
      
        while queue:
            start_index = queue[0][1]
            max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            
            for _ in range(len(queue)):
                node, index = queue.popleft()
                index -= start_index
                print(node.val, index)
                if node.left:
                    queue.append((node.left, 2*index + 1))
                if node.right:
                    queue.append((node.right, 2*index + 2))
            
        return max_width
        
 # using next_queue and no deque  
        
        # if not root: return 0
        
        # max_width = 1
        # queue = [(root, 0)]
      
        # while queue:
        #     next_queue = []
        #     max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            
        #     for _ in range(len(queue)):
        #         node, index = queue.pop(0)
        #         #print(node.val, index)
        #         if node.left:
        #             next_queue.append((node.left, 2*index + 1))
        #         if node.right:
        #             next_queue.append((node.right, 2*index + 2))
        #     queue = next_queue
            
        # return max_width
    
# O(n) time and O(n) space    
# https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/3436593/Image-Explanation-Why-long-to-int-C%2B%2BJavaPython