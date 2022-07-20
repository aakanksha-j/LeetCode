class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])
        stack = []
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows -1) or c in (0, cols - 1)) and board[r][c] == 'O':
                    stack.append((r, c))

                    while stack:
                        nr, nc = stack.pop()
                        board[nr][nc] = 'T'
                        for x, y in dirs:
                            row, col = nr + x, nc + y
                            if 0 <= row < rows and 0 <= col < cols and board[row][col] == 'O':
                                stack.append((row, col))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
