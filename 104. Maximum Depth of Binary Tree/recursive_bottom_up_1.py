"""Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100 """


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        # 1 denotes counting root node

def main():
    numbers = [3,9,20,None,None,15,7]
    s=Solution()
    print(s.maxDepth(numbers))
    numbers = [1,None,2]
    print(s.maxDepth(numbers))
    numbers = []
    print(s.maxDepth(numbers))

if __name__ == '__main__':
    main()

#https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/534/
#https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/34195/Two-Java-Iterative-solution-DFS-and-BFS
