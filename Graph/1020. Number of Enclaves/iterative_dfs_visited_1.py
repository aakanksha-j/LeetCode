# similar to max area of island

# O(m.n) time and space

# iterative dfs solution using visited set

from typing import List 

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        enclaves_count = 0
        ROWS, COLUMNS = len(grid), len(grid[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        visited = set()
        
        for row in range(ROWS):
            for column in range(COLUMNS):  
                if grid[row][column] and (row, column) not in visited:
                    stack = [(row, column)]
                    land_cells = 0
                    flag = True
                    while stack:
                        r, c = stack.pop()
                        if r < 0 or r == ROWS or c < 0 or c == COLUMNS or (r,c) in visited or not grid[r][c]:
                            continue
                        if r == 0 or r == ROWS - 1 or c == 0 or c == COLUMNS - 1:
                            flag = False
                        land_cells += 1
                        visited.add((r,c))
                        stack.append((r+1, c))
                        stack.append((r, c-1))
                        stack.append((r-1, c))
                        stack.append((r, c+1))
                    enclaves_count += land_cells if flag else 0
            
        return enclaves_count
    