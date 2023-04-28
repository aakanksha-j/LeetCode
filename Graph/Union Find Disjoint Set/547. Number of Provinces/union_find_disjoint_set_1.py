"""547. Number of Provinces
Medium
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        rows, cols = len(isConnected), len(isConnected[0])
        
        # disjoint set 
        root = [i for i in range(rows)]
        rank = [1] * rows
        
        def find(vertex):
            x = vertex
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
            
        def union(x, y):
            rootX, rootY = find(x), find(y)
            
            if rootX == rootY:
                return 0
            
            if rank[rootX] > rank[rootY]:
                root[rootY] = rootX
                rank[rootX] += rank[rootY]
            else:
                root[rootX] = rootY
                rank[rootY] += rank[rootX]
                
            return 1
            
        
        count = rows
        for row in range(rows):
            for col in range(cols):
                if row != col and isConnected[row][col] == 1:
                    count -= union(row, col)
        return count