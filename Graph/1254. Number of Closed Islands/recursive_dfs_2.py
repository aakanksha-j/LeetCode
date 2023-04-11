class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        closed_islands = 0
        
        ROWS, COLUMNS = len(grid), len(grid[0])
        
        visited = set()
        
        def dfs(r, c):
            if (r < 0 or r == ROWS or 
               c < 0 or c >= COLUMNS):
                    return 0 # False
            if grid[r][c] == 1 or (r,c) in visited:
                return 1 # True
                 
            visited.add((r,c))
            
            return min(dfs(r+1, c), 
                       dfs(r-1, c), 
                       dfs(r, c+1), 
                       dfs(r, c-1))
       
        for row in range(ROWS):
            for column in range(COLUMNS):
                if grid[row][column] == 0 and (row, column) not in visited:
                    closed_islands += dfs(row, column)
        
        return closed_islands
        
