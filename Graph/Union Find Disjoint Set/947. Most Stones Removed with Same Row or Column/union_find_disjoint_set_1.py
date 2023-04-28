"""947. Most Stones Removed with Same Row or Column
Medium
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 

Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 104
No two stones are at the same coordinate point.
"""
#https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/2812641/python3-DFS-oror-BFS-oror-Union-Find-explained!

# using union find

# time - O(N) we visit each vertex only once
# space - O(N) for union find hashmap

from collections import deque, defaultdict
from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = {}
        
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            if x not in uf:
                uf[x] = x
            if y not in uf:
                uf[y] = y
            rootX = find(x)
            rootY = find(y)
            uf[rootX] = rootY
        
        # range of x,y: 0 to 10^4 
        maxX = 10**4
        for x, y in stones:
            union(x, y + maxX)
                
        return len(stones) - len({find(key) for key in uf})
    
# 11000
# 11000
# 01100
# 00111
# 00011

# uf {0,1,2,3,4,10^4,10^4+1,10^4+2...} will have 10 keys and value of all 10 keys will be 10^4 + 4

# therefore return will be 11 - 1 = 10 stones can be removed

        