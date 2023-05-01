"""
1697. Checking Existence of Edge Length Limited Paths
Hard
An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

 

Example 1:


Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.
Example 2:


Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Exaplanation: The above figure shows the given graph.
 

Constraints:

2 <= n <= 105
1 <= edgeList.length, queries.length <= 105
edgeList[i].length == 3
queries[j].length == 3
0 <= ui, vi, pj, qj <= n - 1
ui != vi
pj != qj
1 <= disi, limitj <= 109
There may be multiple edges between two nodes.
"""
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/discuss/3464923/python-build-graph-from-smallest-dist-to-bigger
        
        # sort queries by limit, sort edge by dist
        # iterate over sorted queries
        #   connect edges u,v with dist < l
        #   check current queries p and q found in same component
        # repeat for all queries with increasing limit
        
        # time O(n + eloge + qlogq) - n for root and rank arrays, eloge to sort edgeList and qlogq to sort queries arrays (for find and union methods inside for loop.. while loop e+q time < eloge + qlogq)
        # space O(n + q) - n for root and rank arrays and sort edgeList array in place, q for sorted queries array
        
        root = [i for i in range(n)]
        rank = [1] * n
        
        def find(vertex):
            x = vertex
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            
            if rootX == rootY:
                return
            
            if rank[rootX] > rank[rootY]:
                root[rootY] = rootX
                rank[rootX] += rank[rootY]
            else:
                root[rootX] = rootY
                rank[rootY] += rank[rootX]
            
            
        q_len, e_len = len(queries), len(edgeList)
        res = [False] * q_len
        
        edgeList.sort(key = lambda x: x[2])
        queries = sorted(((u,v,l,i) for i,(u,v,l) in enumerate(queries)), key = lambda x: x[2])
        
        e_idx = 0
        for p, q, l, i in queries:
            while e_idx < e_len and edgeList[e_idx][2] < l:
                u, v, _ = edgeList[e_idx]
                union(u, v)
                e_idx += 1
            res[i] = find(p) == find(q)

        return res