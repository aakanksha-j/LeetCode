class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        while stack or root:
            if root:
                stack.append(root) # append root and not left
                root = root.left
            else:
                tmpNode = stack.pop()
                res.append(tmpNode.val)
                root = tmpNode.right
        return res

# [1,null,2,3]
# stack = [TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: None}}]
# time and space complexity: O(n)
# same logic as recursion instead switched to iteration
