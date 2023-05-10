"""59. Spiral Matrix II
Medium
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20"""

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        first_row, first_col = 0, 0
        last_row, last_col = n-1, n-1
        output = [[0]*n for _ in range(n)]
        num = 1
        while first_row <= last_row and first_col <= last_col:
            for j in range(first_col, last_col + 1):
                output[first_row][j] = num
                num += 1
            first_row += 1
            for i in range(first_row, last_row + 1):
                output[i][last_col] = num
                num += 1
            last_col -= 1
            for j in range(last_col, first_col - 1, -1):
                output[last_row][j] = num
                num += 1
            last_row -= 1
            for i in range(last_row, first_row - 1, -1):
                output[i][first_col] = num
                num += 1
            first_col += 1
        return output
    
# https://leetcode.com/problems/spiral-matrix-ii/discuss/22290/Python-easy-to-follow-solution.

# time O(n^2)
# space O(1)