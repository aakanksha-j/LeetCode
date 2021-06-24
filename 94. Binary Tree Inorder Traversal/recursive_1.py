"""Given the root of a binary tree, return the preorder traversal of its nodes' values.
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [1,2]

Example 6:
Input: root = [6,2,7,1,4,null,9,null,null,3,5,8,null]
Output: [1,2,3,4,5,6,7,8,9]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            res.append(root.val)
            self.dfs(root.right, res)

    def inorderTraversal(self, root: TreeNode):
        res = []
        self.dfs(root, res)
        return res

def main():
    numbers = [1,None,2,3]
    s=Solution()
    print(s.inorderTraversal(numbers))
    numbers = []
    print(s.inorderTraversal(numbers))
    numbers = [6,2,7,1,4,null,9,null,null,3,5,8,null]
    print(s.inorderTraversal(numbers))

if __name__ == '__main__':
    main()
