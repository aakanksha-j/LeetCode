"""323. Number of Connected Components in an Undirected Graph
Medium

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.

"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # neetcode solution
        
        # path compression and union by rank optimization used for disjoint sets.
        
        
        root = [i for i in range(n)]
        rank = [1] * n
        
        def find(edge):
            c = edge
            
            # instead of recursion, while loop for path compression
            while c != root[c]:
                root[c] = root[root[c]]
                c = root[c]
            return c
        
        def union(x, y): 
            rootX, rootY = find(x), find(y)
            
            # no union performed, therefore no increase in rank of parent
            if rootX == rootY:
                return 0
            
            # union by rank
            if rank[rootX] > rank[rootY]:
                root[rootY] = rootX
                rank[rootX] += rank[rootY]
            else:
                root[rootX] = rootY
                rank[rootY] += rank[rootX]
                
            # union performed, so return 1
            return 1               
            
        
        output = n
        for edge1, edge2 in edges:
            output -= union(edge1, edge2)
      
        return output
            