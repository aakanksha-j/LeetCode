class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(board, r, c, num):
            # check row
            for i in range(9):
                if board[i][c] == num:
                    return False
            # check column
            for j in range(9):
                if board[r][j] == num:
                    return False
            # check square
            for i in range(3):
                for j in range(3):
                    if board[i + (r // 3)* 3][j + (c // 3) * 3] == num:
                        return False
            return True

        def solve(board):
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c] == '.':
                        for num in "123456789":
                            if isValid(board, r, c, num):
                                board[r][c] = num
                                if solve(board):
                                    return True
                                else:
                                    board[r][c] = '.'
                        return False # tried all numbers from 1 to 9, nothing worked, no solution possible
            return True

        solve(board)
#https://leetcode.com/problems/sudoku-solver/discuss/15752/Straight-Forward-Java-Solution-Using-Backtracking

# time: brute force - 9^81
#       Backtracking - (9!)^9 9! ways to fill first row, 9!.9!.9!.... for 9 rows
# space: O(1) since we modify board in place. 81 elements 
