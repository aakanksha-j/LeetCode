class Solution:
    # without visited set, input will be modified
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

"""Iterate through each of the cell and if it is an island, do dfs to mark all adjacent islands, then increase the counter by 1.
https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution"""


# with visited set, input will not be modified, the set will take extra space.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs recursive with visited set to not modify input

        m, n = len(grid), len(grid[0])
        count, visited = 0, set()

        # drown the connected landmass
        def dfs(r, c, grid, visited):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1' or (r,c) in visited:
                return

            visited.add((r,c))

            dfs(r + 1, c, grid, visited)
            dfs(r - 1, c, grid, visited)
            dfs(r, c + 1, grid, visited)
            dfs(r, c - 1, grid, visited)

        # iterate over matrix to find an island
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    count += 1
                    dfs(i, j, grid, visited)

        return count
