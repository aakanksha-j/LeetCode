class Solution:
    def binary_search(self, arr, left, right, target):

        # 1st matrix's col passed as target, find the row with same value in 2nd matrix
        while left <= right:
            mid = (left + right) // 2
            if target == arr[mid][0]:
                return mid
            elif target < arr[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # one longer than other, both are sparse, use binary search from 1570 on index, value pairs


        m, n, k = len(mat1), len(mat2[0]), len(mat1[0])
        if k != len(mat2):
            raise Exception("1st matrix's column number must be equal to 2nd matrix's row number.")
        output = [[0 for _ in range(n)] for _ in range(m)]

        # build (row, col, val) pair for both matrices to convert 2d matrix into 1d vector representation
        v1 = []
        for i in range(m):
            for j in range(k):
                if mat1[i][j]:
                    v1.append((i, j, mat1[i][j]))
        print(v1)
        v2 = []
        for i in range(k):
            for j in range(n):
                if mat2[i][j]:
                    v2.append((i, j, mat2[i][j]))
        print(v2)

        if not v1 or not v2: return output

        # run binary search on 2nd matrix and add to output wherever 1st matrix's col = 2nd matrix's row
        
        for i, j, val in v1:
            print(i,j,val)
            idx = self.binary_search(v2, 0, k - 1, j)
            print(v2[idx])
            if idx != -1:
                output[i][v2[idx][1]] += val * v2[idx][2]

        #therefore, used 2 for loops
        for i, j, val1 in v1:
            for x, y, val2 in v2:
                if j == x:
                    output[i][y] += val1 * val2
        # next, will use 2 pointers merge sort
        return output

"""
class Solution:
    # time: O(n^2)
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        sparse_A = self.get_none_zero(A)
        sparse_B = self.get_none_zero(B)
        n, m, k = len(A), len(A[0]), len(B[0])
        C = [[0] * k for _ in range(n)]
        for i, j, val_A in sparse_A:
            for x, y, val_B in sparse_B:
                if j == x:
                    C[i][y] += val_A * val_B
        return C

    def get_none_zero(self, A):
        res = []
        n, m = len(A), len(A[0])
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    continue
                res.append((i, j, A[i][j]))
        return res
"""

# binary search not working on dense data such as
        # mat1 = [[1,1,1],[1,1,1],[1,1,1]]
        # mat2 = [[1,1,1],[1,1,1],[1,1,1]]
        # output = [[3,3,3],[3,3,3],[3,3,3]]