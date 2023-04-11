from typing import List 

# fastest solution

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])
        def dfs(i,j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0 
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
        for i in [0,m-1]:
            for j in range(n):
                dfs(i,j)
        for i in range(m):
            for j in [0,n-1]:
                dfs(i,j)
        return sum(sum(i) for i in grid)
    

# dfs recursive solution from neetcodeio using visited set 
# O(m.n) time and space

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        ROWS, COLUMNS = len(grid), len(grid[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        visited = set()
        land_cells, border_land = 0, 0
        
        def dfs(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLUMNS or (r,c) in visited or not grid[r][c]:
                return 0
            res = 1
            visited.add((r,c))
            return res + dfs(r+1, c) + dfs(r, c-1) + dfs(r-1, c) + dfs(r, c+1)
        
        for row in range(ROWS):
            for column in range(COLUMNS):  
                land_cells += grid[row][column]
                if grid[row][column] and (row, column) not in visited and (
                    row in [0, ROWS-1] or column in [0, COLUMNS - 1]):
                    border_land += dfs(row, column)
                    
        return land_cells - border_land