"""
1351. Count Negative Numbers in a Sorted Matrix
Easy

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 

Follow up: Could you find an O(n + m) solution?
"""

# own solution using binary search
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count_negative = 0
        ROWS, COLUMNS = len(grid), len(grid[0])
        last_negative_col = COLUMNS - 1
        for row in range(ROWS):
            l, r = 0, last_negative_col
            while l < r:
                mid = (l + r)//2 
                if grid[row][mid] < 0:
                    r = mid
                else:
                    l = mid + 1
            #print(l, r)
            if l < COLUMNS and grid[row][l] < 0:
                count_negative += COLUMNS - l
                last_negative_col = l
        return count_negative

# leetcode solution using binary search
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # using binary search
        # time: O(m logn), space: O(1)
    
        count_negative = 0
        ROWS, COLUMNS = len(grid), len(grid[0])
        for row in grid:
            l, r = 0, COLUMNS - 1
            while l <= r:
                mid = (l + r)//2 
                if row[mid] < 0:
                    r = mid - 1
                else:
                    l = mid + 1
            #print(l, r)
            count_negative += COLUMNS - l
        return count_negative

# leetcode solution using linear traversal
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # using linear traversal
        # time: O(m + n), space: O(1)
    
        count_negative = 0
        ROWS, COLUMNS = len(grid), len(grid[0])
        r = COLUMNS - 1
        for row in grid:
            while r >= 0 and row[r] < 0:
                r -= 1
            print(r)
            if r < 0:
                count_negative += COLUMNS
            else:
                count_negative += COLUMNS - (r+1)
        return count_negative
                
