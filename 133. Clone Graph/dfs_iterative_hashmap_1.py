"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # dfs iterative hashmap space

        # 3 test cases: input = [], [[]], [[2,4], [1,3], [2,4], [1,3]]

        # input is an empty graph (has no nodes: [])
        if not node:
            return None # why return None or node and not []

        #print(node.val) # input: [[]] has 1 node, no neighbors, output: [[]]

        deepcopy = {None: None}
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur not in deepcopy:
                deepcopy[cur] = Node(cur.val)
            if cur.neighbors:
                for neighbor in cur.neighbors:
                    if neighbor not in deepcopy:
                        #print(neighbor.val)
                        deepcopy[neighbor] = Node(neighbor.val)
                        stack.append(neighbor)
                    deepcopy[cur].neighbors.append(deepcopy[neighbor])

        return deepcopy[node]

# similar to copy list with random pointer, clone binary tree, clone n-ary tree
# we use extra space of a dictionary to create deepcopy
# for bfs, instead of while stack, while queue and stack.pop, do queue.popleft()
# time complexity: ?O(n+m) for n vertices (neighbors) and m edges (cur nodes)
# space complexity: O(n) for n vertices (neighbors)

"""https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).""""
