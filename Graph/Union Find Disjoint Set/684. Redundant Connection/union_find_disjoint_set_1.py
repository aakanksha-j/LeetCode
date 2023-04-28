"""684. Redundant Connection
Medium
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # neetcode solution
        
        # use union find methods of disjoint set
        # using dfs, O(n2) time complexity, using union find O(n)
        # space needed is O(n) for root and rank arrays
        
        # for the edges given, union the vertices in the given edge eg.(1,4)
        # if during union, we encounter that root of both nodes is same,
        # then that means, union is already performed and we have found the
        # redundant edge, no need to perform union again, return False, return 
        # that edge as output
        # until then, keep performing union find function as earlier, return True
        
        # declare root and rank arrays for nodes
        root = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        # find method  # using recursion instead of iteration
        def find(vertex):
            x = vertex
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
            
        # union method
        def union(x, y):
            # find root of x and y
            rootX, rootY = find(x), find(y)
            
            # 3 cases
            # 1. root of both x and y are same, union already performed
            if rootX == rootY:
                return False
            
            # 2. height of tree of X is higher than Y
            if rank[rootX] > rank[rootY]:
                root[rootY] = rootX
                rank[rootX] += rank[rootY]
            else: # 3. rank of y is higher than x, more elements on Y's side
                root[rootX] = rootY
                rank[rootY] += rank[rootX]
                
            return True
            
            
        # traverse all the edges, return the edge which returns False
        for edge1, edge2 in edges:
            if not union(edge1, edge2):
                return [edge1, edge2]
        
            