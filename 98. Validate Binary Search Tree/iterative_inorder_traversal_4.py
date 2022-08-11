# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # iterative inorder traversal solution - leetcode 94 on 8 11 2022        

        prev = -math.inf

        stack = []
        r = root
        while stack or r:
            if r:
                stack.append(r)
                r = r.left
            else:
                node = stack.pop()
                if node.val <= prev:
                    return False
                r, prev = node.right, node.val

        return True


"""previous code 2 :
        # BST definition: left < root < right

        # time: O(N) - have to traverse entire tree once, worst case is when tree is BST or bad leaf is rightmost leaf
        # space: O(N) - to keep stack

        # approach: append elements in inorder traversal order, basically append all left elements to stack. Then compare current value with previous value i.e left node (eg. in 4,2,5,1,6) pre=6 and node=4 (1,2,6,4,5)

        if not root: return True

        node, pre = root, -math.inf
        stack = []

        while stack or node:

            # keep adding to stack until left node exists
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            print(node.val, pre)

            if node.val <= pre:
                return False

            node, pre = node.right, node.val
            # when node.right = None, parent of node will be popped, and node will be pre


        return True

previous code 1:
        stack, prev = [], -math.inf
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if node.val <= prev:
                return False
            prev = node.val
            root = node.right
        return True"""
