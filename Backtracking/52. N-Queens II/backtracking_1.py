class Solution:
    def totalNQueens(self, n: int) -> int:
        # based on solution used in N-Queens


        board = [['.'] * n for _ in range(n)]
        cols = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        def backtrack(r):
            if r == n:
                return 1

            output = 0
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'

                output += backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'

            return output


        return backtrack(0)
        
