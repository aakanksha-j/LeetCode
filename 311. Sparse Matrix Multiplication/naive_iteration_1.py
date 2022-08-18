class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # own approach

        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        output = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for x in range(n):
                for j in range(k):
                    if mat1[i][j] == 0:
                        continue
                    if mat2[j][x] == 0:
                        continue
                    output[i][x] += mat1[i][j] * mat2[j][x]

        return output
                
