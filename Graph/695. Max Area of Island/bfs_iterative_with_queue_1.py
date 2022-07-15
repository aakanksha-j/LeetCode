class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Graph sum - bfs iterative with queue
        # similar to 490 maze and 200 no of islands
        # solved on my own

        max_count = 0

        m = len(grid) # length of rows
        n = len(grid[0]) # length of columns

        # identify new island using for loops
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                count = 0

                if grid[i][j] == 1:
                    count += 1

                    # add to queue so that we can use popleft
                    # we need to drown surrounding islands so bfs, instead of dfs
                    q = collections.deque([[i,j]])
                    # mark as visited when queued
                    grid[i][j] = 2

                    while q:
                        r,c = q.popleft()

                        # use dirs set to move in all 4 directions
                        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

                        for x, y in dirs:
                            row = r + x
                            col = c + y

                            while 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                                q.append([row,col]) # add to queue
                                grid[row][col] = 2 # mark as visited when queued
                                count += 1

                                row += x
                                col += y
                            row -= x
                            col -= y
                    max_count = max(max_count, count)

        return max_count
