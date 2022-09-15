class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # bfs using queue as we can do popleft
        # no extra space, input maze is modified , visited array not used
        # for bfs, we marked the node as visited (maze[row][col] =2)
        # when it is enqueued, not when we visit it.

        m, n = len(maze), len(maze[0])  #row - m, column - n
        dirs = ((0,1), (1,0), (0,-1), (-1,0))

        q = collections.deque([start])
        maze[start[0]][start[1]] = 2
        while q:
            i,j = q.popleft()

            if i == destination[0] and j == destination[1]:
                return True

            for x, y in dirs:
                row = i + x
                col = j + y

                # keep increasing until we hit a wall
                while 0 <= row < m and 0 <= col < n and maze[row][col] == 0:
                    row += x
                    col += y
                row -= x
                col -= y

                if maze[row][col] == 0:
                    #print(maze)
                    q.append([row, col])
                    maze[row][col] = 2

        return False

"""https://leetcode.com/problems/the-maze/discuss/97074/Python-BFS-solution
https://leetcode.com/problems/the-maze/discuss/198453/Python-BFS-tm"""

#dfs_pop_no_extra_space_1
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # dfs using stack using pop and marking as visited after popping

        m, n = len(maze), len(maze[0])  #row - m, column - n
        dirs = ((0,1), (1,0), (0,-1), (-1,0))

        q = [start]

        while q:
            i,j = q.pop()
            maze[i][j] = 2

            if i == destination[0] and j == destination[1]:
                return True

            for x, y in dirs:
                row = i + x
                col = j + y

                # keep increasing until we hit a wall
                while 0 <= row < m and 0 <= col < n and maze[row][col] == 0:
                    row += x
                    col += y
                row -= x
                col -= y

                if maze[row][col] == 0:
                    q.append([row, col])

        return False
