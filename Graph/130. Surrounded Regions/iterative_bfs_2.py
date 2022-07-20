from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # iterative bfs using queue, iterative dfs using stack already implemented

        # time: O(N) - iterate over entire array if all cells are 'O'
        # space: O(N) - at any time, queue or stack may contain elements of two levels which might be proportional to number of cells in entire array

        q = collections.deque([])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        rows, cols = len(board), len(board[0])


        # don't forget its range(rows) and not for r in rows
        for r in range(rows):
            for c in range(cols):
                # dont forget () for r,c before and
                if (r in (0, rows - 1) or c in (0, cols - 1)) and board[r][c] == 'O':
                    q.append((r, c))

        while q:
            row, col = q.popleft()
            board[row][col] = 'T'
            for x, y in dirs:
                nr, nc = row + x, col + y
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
