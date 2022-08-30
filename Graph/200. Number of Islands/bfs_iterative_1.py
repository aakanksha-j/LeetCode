import collections

class Solution:

    def numIslands(self, grid) -> int:
        # bfs to drown island (connected '1') and for loop to identify new island
        # solved after 490 The maze (Graph)


        m = len(grid) # length of rows
        n = len(grid[0]) # length of columns

        count = 0
        # identify start of island using nested for loops
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                # increase count whenever island found
                if grid[i][j] == "1":
                    count += 1

                    # similar to maze sum, use dirs set to move
                    dirs = ((1,0), (-1,0), (0,1), (0,-1))

                    # since it is bfs, mark as visited when enqueued
                    grid[i][j] = "2"
                    # use collections for popleft
                    q = collections.deque([[i,j]])
                    while q:
                        r,c = q.popleft()

                        for x,y in dirs:
                            row = r + x
                            col = c + y

                            # keep going until we find water or visited landmass
                            while 0 <= row < m and 0 <= col < n and grid[row][col] == "1":
                                q.append([row,col]) # enqueue connected land mass
                                # will not be counted again during for loop
                                grid[row][col] = "2" # mark as visited when enqueued

                                row += x # move forward
                                col += y
                            row -= x # move backward, reached water '0' or queued landmass '2'
                            col -= y

        return count


def main():
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    print(grid)
    s=Solution()
    print(s.numIslands(grid))

if __name__ == '__main__':
    main()


"""https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution

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
"""
