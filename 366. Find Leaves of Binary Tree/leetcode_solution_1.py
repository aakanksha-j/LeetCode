# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = []

    def getHeight(self, root):
        # return -1 for null nodes
        if not root:
            return -1

        # calculate height for left and right children
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        currHeight = 1 + max(leftHeight, rightHeight)

        if len(self.output) == currHeight:
            self.output.append([])

        self.output[currHeight].append(root.val)

        return currHeight

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.getHeight(root)

        return self.output


"""Shorter version
def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # leetcode solution without initializing output in init and dfs method inside findLeaves

        output = []

        def dfs(root, output):
            if not root:
                return -1

            height = 1 + max(dfs(root.left, output), dfs(root.right, output))

            if height >= len(output):
                output.append([])

            output[height].append(root.val)

            return height

        dfs(root, output)

        return output"""
