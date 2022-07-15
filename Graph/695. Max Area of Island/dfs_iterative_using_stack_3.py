class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs iterative using stack
        # leetcode solution

        # time: O(row. col) - traverse the entire matrix only once
        # space: O(row.col) - space used by visited set

        visited = set() # (r,c)

        rows, cols = len(grid), len(grid[0])
        stack = []
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        max_area = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    cur_area = 0
                    stack = [(row, col)]
                    visited.add((row, col))
                    while stack:
                        r,c = stack.pop()
                        cur_area += 1
                        for x, y in dirs:
                            nr, nc = r + x, c + y
                            if (0 <= nr < len(grid) and
                                0 <= nc < len(grid[0]) and
                                (nr, nc) not in visited and
                                grid[nr][nc] == 1):
                                stack.append((nr, nc))
                                visited.add((nr, nc))
                    max_area = max(max_area, cur_area)

        return max_area
