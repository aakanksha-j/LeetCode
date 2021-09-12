"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # using 3 loops and 4 array variables
        if not root: return []
        res = []
        cur_stack = [root]
        while cur_stack:
            tmp, nxt_stack = [], []
            for node in cur_stack:
                tmp.append(node.val)
                for child in node.children:
                    nxt_stack.append(child)
            cur_stack = nxt_stack
            res.append(tmp)
        return res

"""In Binary tree, this approach was very slow. Therefore, learn a more optimal
solution.
https://leetcode.com/problems/n-ary-tree-level-order-traversal/discuss/162439/Python-iterative-solution-beat-96"""

from collections import deque

class Solution:
    # bfs using deque
    def levelOrder(self, root):
        res, queue = [], deque()
        if root:
            queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append(tmp)
        return res

"""O(n) time and O(n) space to store elements in queue (output res space not counted).
https://leetcode.com/problems/n-ary-tree-level-order-traversal/discuss/1386593/C%2B%2BPython-BFS-and-DFS-Solutions-Clean-and-Concise"""
