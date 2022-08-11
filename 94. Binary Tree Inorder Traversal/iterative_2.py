class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative inorder traversal solution - leetcode 94 on 8 11 2022

        if not root:
            return []

        r, stack, output = root, [], []
        while stack or r:
            if r: # append left nodes
                stack.append(r)
                r = r.left
            else: # left added to the result, now because left is None, root is popped
                node = stack.pop()
                output.append(node.val)
                r = node.right # append right nodes, not to stack but to r

        return output

"""previous code

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

                """
