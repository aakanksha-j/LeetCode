"""
1579. Remove Max Number of Edges to Keep Graph Fully Traversable
Hard

Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

Constraints:

1 <= n <= 105
1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
edges[i].length == 3
1 <= typei <= 3
1 <= ui < vi <= n
All tuples (typei, ui, vi) are distinct."""

# refer to leetcode solution - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/solution/

# time - O(E. Ackermann function(N)) - E no. of edges, N no. of nodes
# space - O(N) - for root and rank arrays containing N nodes

from typing import List


class DSU:
    def __init__(self, n):
        self.root = [i for i in range(n+1)] # because edges are numbered from 1 to n
        self.rank = [1] * (n+1)
        self.components = n
        
    def find(self, vertex):
        x = vertex
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX == rootY:
            return 0

        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
        else:
            self.root[rootX] = rootY
            self.rank[rootY] += self.rank[rootX]
        self.components -= 1
        return 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # connect all edges for both objects Bob and alice
        # first connect using type 3 to minimize edges required
        # next use personalized edges and assign redundant immediately if not used
        # at the end, return the count of total edges - edges required
                
        alice = DSU(n)
        bob = DSU(n)
        edges_reqd = 0
        for typ, src, dst in edges:
            if typ == 3:
                edges_reqd += alice.union(src, dst)
                bob.union(src, dst)
          
        for typ, src, dst in edges:
            if typ == 1:
                edges_reqd += alice.union(src, dst)    
            if typ == 2:
                edges_reqd += bob.union(src, dst)    
        
        if alice.components == bob.components == 1:
            return len(edges) - edges_reqd
        return -1