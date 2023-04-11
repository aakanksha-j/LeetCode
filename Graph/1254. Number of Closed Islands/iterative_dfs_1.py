"""1254. Number of Closed Islands
Medium

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""

# dfs iterative using stack with visited set
from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        

        # time - O(m.n) iterate every element in matrix
        # space - O(m.n) for visited set

        ROWS, COLUMNS = len(grid), len(grid[0])
        closed_islands = 0
        visited = set()
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                stack = []
                if grid[row][column] == 0 and (row, column) not in visited:
                    stack.append((row,column))
                    flag = True
                    while stack:
                        r, c = stack.pop()
                        if (r < 0 or r == ROWS or c < 0 or c == COLUMNS or grid[r][c] == 1 or (r,c) in visited):
                            continue
                        if (r == 0 or r == ROWS-1 or c == 0 or c == COLUMNS - 1):
                            flag = False
                        visited.add((r,c))
                        stack.append((r+1, c))
                        stack.append((r, c-1))
                        stack.append((r-1, c))
                        stack.append((r, c+1))
                    closed_islands += flag
        
        return closed_islands
    
# even after making flag false, continue to add it to visited and find its neighbors
        

        