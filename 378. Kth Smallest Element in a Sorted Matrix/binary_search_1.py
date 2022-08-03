# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1322101/C%2B%2BJavaPython-MaxHeap-MinHeap-Binary-Search-Picture-Explain-Clean-and-Concise

class Solution:
    # binary search solution - for utilizing sorted array and constant space 
    # time: O(n. log(n))
    # space: O(1)
    def count_less_or_equal(self, matrix, mid, smaller, larger):
        cnt, n = 0, len(matrix)
        row, col = n - 1, 0

        while row >= 0 and col < n: # inspired from 240 Search in 2D Matrix II solution
            if matrix[row][col] <= mid:
                cnt += row + 1
                col += 1
            else:
                row -= 1

        return cnt

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[n - 1][n - 1]
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            cnt = self.count_less_or_equal(matrix, mid, left, right)

            if cnt >= k:
                ans = mid
                right = mid - 1 # search in left array from mid
            else:
                left = mid + 1 # search in right array from mid

        return ans
