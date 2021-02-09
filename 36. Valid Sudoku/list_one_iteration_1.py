class Solution:
    """Approach 1: Using List to store elements in a row, column and box.
       Time complexity: O(1)
       Space complexity: O(1) because constant space of 3 lists with 9 lists
                         nested in them.
       Runtime: 84 ms
       Memory: 14.2 MB
    """
    def isValidSudoku(self, board) -> bool:
        row = [[] for i in range(9)]
        col = [[] for i in range(9)]
        box = [[] for i in range(9)]

        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit != '.':
                    digit = int(digit)
                    if digit not in row[i]:
                        row[i].append(digit)
                    else:
                        return False
                    if digit not in col[j]:
                        col[j].append(digit)
                    else:
                        return False
                    box_idx = ((i // 3) * 3) + (j // 3)
                    if digit not in box[box_idx]:
                        box[box_idx].append(digit)
                    else:
                        return False
        print(row)
        print(col)
        print(box)
        return True

def main():
    board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    s=Solution()
    print(s.isValidSudoku(board))
    board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    print(s.isValidSudoku(board))

if __name__ == '__main__':
    main()
