# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not preorder:
            return None

        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)

        ptr_pre, ptr_in = 1, 0

        while ptr_pre < len(preorder):

            curr = TreeNode(preorder[ptr_pre])
            ptr_pre += 1
            prev = None

            while stack and stack[-1].val == inorder[ptr_in]:
                prev = stack.pop()
                ptr_in += 1

            if prev:
                prev.right = curr
            else:
                stack[-1].left = curr

            stack.append(curr)

        return root

"""This question is basically reverse of inorder traversal. In iterative solution
of inorder traversal, we continue to add the nodes starting from root node on to
the stack until there are no left nodes left. Then we start popping the stack
elements, add the element to output list, followed by adding their right node.

Here we create the root node from preorder. Inside while loop, create a temp
curr node. Use another while loop to see if the last element in stack is also
equal to the inorder value. Pop element from stack if they match and increase the
counter in inorder. Use the popped value as a flag. If the flag is set, insert
curr node to right of flag. Else, make curr node as left element to the last
element of stack. Add curr to stack.

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34555/The-iterative-solution-is-easier-than-you-think!"""
