class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # neetcode solution

        # time complexity: O(N!) as after every row traversal we have N, N - 2, N - 4 etc.
        # space complexity: O(N^2) for storing state of board of size N*N. 3 Sets and recursive calls take O(N) space, linear with number of queens

        # 1. initialize output, board, 3 sets - cols, posDiag, negDiag
        # 2. Call backtrack funtion, return output
        # 3. inside backtrack function, if number of rows is equal to n, append copy to output and return
        # 4. run for loop for columns, check 3 sets, add to them and make that location 'Q',
        # if place available, not skipped iteration using continue, then dfs next row using backtranck method
        # if no place found, then backtrack the sets and 'Q' to '.'

        output = []
        board = [['.'] * n for _ in range(n)] # similar to transpose matrix sum
        # [[None]*rows for _ in range(cols)]
        cols = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        def backtrack(r):
            # dfs recursion base case - placed all the queens without attacking each other
            if r == n:
                copy = [''.join(row) for row in board] # convert array of dots to string of dots ['.','.','.','.'] -> ['....']
                output.append(copy)
                return

            # iterate through columns
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'


        backtrack(0)

        return output
