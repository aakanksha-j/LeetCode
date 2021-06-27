"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def dfs(self, root, res):
        if root:
            for child in root.children:
                self.dfs(child, res)
            res.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.dfs(root, res)
        return res

# Input: root = [1,null,3,2,4,null,5,6]
# Output: [5,6,3,2,4,1]

# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
