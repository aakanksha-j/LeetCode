"""54. Spiral Matrix
Medium
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        first_row, first_col = 0, 0
        last_row, last_col = m-1, n-1
        output = []
        while first_row <= last_row and first_col <= last_col:
            for j in range(first_col, last_col + 1):
                output.append(matrix[first_row][j])
            first_row += 1
            for i in range(first_row, last_row + 1):
                output.append(matrix[i][last_col])
            last_col -= 1
            if first_row <= last_row:
                for j in range(last_col, first_col - 1, -1):
                    output.append(matrix[last_row][j])
                last_row -= 1
            if first_col <= last_col:
                for i in range(last_row, first_row - 1, -1):
                    output.append(matrix[i][first_col])
                first_col += 1
        return output
    
# time O(m.n)
# space O(1)

# https://leetcode.com/problems/spiral-matrix/discuss/20820/Python-easy-to-understand-solution-(left-right-top-down).