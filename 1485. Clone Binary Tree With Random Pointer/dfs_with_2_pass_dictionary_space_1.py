# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        # dfs with 2 pass
        # similar to copy list with random pointer
        # no need to check like clone graph whether node is in deepcopy or not

        # null root input
        if not root:
            return None

        deepcopy = {}

        # 1st pass - traverse tree to create nodes
        stack = [root]
        while stack:
            node = stack.pop()
            deepcopy[node] = NodeCopy(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # 2nd pass - connect the nodes with their pointers
        stack = [root]
        while stack:
            node = stack.pop()

            if node.left:
                deepcopy[node].left = deepcopy[node.left]
                stack.append(node.left)

            if node.right:
                deepcopy[node].right = deepcopy[node.right]
                stack.append(node.right)

            if node.random:
                deepcopy[node].random = deepcopy[node.random]

        return deepcopy[root]
        
