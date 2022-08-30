class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs iterative using stack with visited set

        # time - O(m.n) iterate every element in matrix
        # space - O(m.n) for visited set

        output = 0
        visited = set()
        stack = []
        m, n = len(grid), len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1' and (row,col) not in visited:
                    stack.append((row,col))
                    output += 1
                    while stack:
                        r, c = stack.pop()
                        if (r < 0 or r >= m) or (c < 0 or c >= n) or ((r,c) in visited) or (grid[r][c] == '0'):
                            continue
                        visited.add((r,c))
                        stack.append((r+1, c))
                        stack.append((r, c-1))
                        stack.append((r-1, c))
                        stack.append((r, c+1))
        return output


        
