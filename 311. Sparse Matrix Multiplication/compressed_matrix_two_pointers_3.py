class Solution:
    def multi(self, row, col):
        ans = 0
        m, n = len(row), len(col)
        i, j = 0, 0
        while i < m and j < n:
            index_row, val_row = row[i]
            index_col, val_col = col[j]
            if index_row < index_col:
                i += 1
            elif index_row > index_col:
                j += 1
            else:
                ans += val_row * val_col
                i += 1
                j += 1

        return ans

    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # two pointers using 1d vector - https://leetcode.com/problems/sparse-matrix-multiplication/discuss/577491/4-python-approaches-with-time-and-space-analysis

        # time: O(m.k.n) when both A and B dont have any 0, O(N) where N is the no of nonzero values
        # intention is to ask how we store data to achieve high efficiency

        A, B = mat1, mat2
        m, k, n = len(A), len(A[0]), len(B[0])

        row_vector = [[(j, A[i][j]) for j in range(k) if A[i][j]] for i in range(m)]
        print(row_vector)
        col_vector = [[(i, B[i][j]) for i in range(k) if B[i][j]] for j in range(n)]
        print(col_vector)

        output = [[self.multi(row, col) for col in col_vector] for row in row_vector]
        print(output)

        return output

"""leetcode Solution
class SparseMatrix:
    def __init__(self, matrix: List[List[int]], col_wise: bool):
        self.values, self.row_index, self.col_index = self.compress_matrix(matrix, col_wise)

    def compress_matrix(self, matrix: List[List[int]], col_wise: bool):
        return self.compress_col_wise(matrix) if col_wise else self.compress_row_wise(matrix)

    # Compressed Sparse Row
    def compress_row_wise(self, matrix: List[List[int]]):
        values = []
        row_index = [0]
        col_index = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]:
                    values.append(matrix[row][col])
                    col_index.append(col)
            row_index.append(len(values))

        return values, row_index, col_index

    # Compressed Sparse Column
    def compress_col_wise(self, matrix: List[List[int]]):
        values = []
        row_index = []
        col_index = [0]

        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                if matrix[row][col]:
                    values.append(matrix[row][col])
                    row_index.append(row)
            col_index.append(len(values))

        return values, row_index, col_index

class Solution:
    # yale format
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
            A = SparseMatrix(mat1, False)
            B = SparseMatrix(mat2, True)

            ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]

            for row in range(len(ans)):
                for col in range(len(ans[0])):

                    # Row element range indices
                    mat1_row_start = A.row_index[row]
                    mat1_row_end = A.row_index[row + 1]

                    # Column element range indices
                    mat2_col_start = B.col_index[col]
                    mat2_col_end = B.col_index[col + 1]

                    # Iterate over both row and column.
                    while mat1_row_start < mat1_row_end and mat2_col_start < mat2_col_end:
                        if A.col_index[mat1_row_start] < B.row_index[mat2_col_start]:
                            mat1_row_start += 1
                        elif A.col_index[mat1_row_start] > B.row_index[mat2_col_start]:
                            mat2_col_start += 1
                        # Row index and col index are same so we can multiply these elements.
                        else:
                            ans[row][col] += A.values[mat1_row_start] * B.values[mat2_col_start]
                            mat1_row_start += 1
                            mat2_col_start += 1

            return ans"""

#https://leetcode.com/problems/sparse-matrix-multiplication/discuss/419538/What-the-interviewer-is-expecting-when-this-problem-is-asked-in-an-interview...
#https://github.com/SCIN/Facebook-Interview-Coding-1/blob/master/Sparce%20Matrix%20Multiplication.java
