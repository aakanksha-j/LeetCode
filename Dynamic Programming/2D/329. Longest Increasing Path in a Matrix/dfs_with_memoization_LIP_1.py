class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # neetcode solution

        # create LIP for memoization (mxn matrix, so mxn extra space)
        # time: mxn as we need to traverse every cell in worst case, when the entire matrix is the longest path, or all elements are equal and no path

        # inside dfs:
        # LIP already has the value of previous node, so return that value
        # out of bounds value of row, col or current value is less than prev val
        # add 1 to every direction, take max of all 4 directions,

        # traverse every cell
        # take max of LIP

        rows, cols = len(matrix), len(matrix[0])

        # LIP = {(r,c): value}
        LIP = {} # data structure: dictionary with row, col tuple as key and max length as value


        def dfs(r, c, prev_val):

            # edge case: out of bound row, col, prevval > curval
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                prev_val >= matrix[r][c]):
                return 0

            # if value is already present in LIP, return that value
            if (r,c) in LIP:
                return LIP[(r,c)]

            res = 1
            # check in all 4 directions, moving in diagonal direction not allowed
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            LIP[(r,c)] = res

            return res

        # traverse every cell
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, -1)
        # take max of LIP
        return max(LIP.values())
    
