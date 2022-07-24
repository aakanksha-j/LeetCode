class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # leetcode solution - search space reduction

        # time: O(m+n) - either we will decrement row or increment col so we can
        #                only move in worst case in m ways and n ways, so m+n and
        #                not m.n
        # space: O(1)

        i,j = len(matrix) - 1, 0
        while 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
            # print(i, j, matrix[i][j])
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j]:
                i -= 1
            else:
                j += 1

        return False
