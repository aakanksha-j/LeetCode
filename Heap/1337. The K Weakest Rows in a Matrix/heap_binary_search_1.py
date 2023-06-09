"""1337. The K Weakest Rows in a Matrix
Easy
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

 

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].
Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
 

Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
"""
# approach 1: own using heap

import heapq
from typing import List

# m = len(rows), n = len(columns)

# time O(m.n + mlogm)
# space O(m)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength_index_heap = []
        for i in range(len(mat)):
            strength_index_heap.append((sum([x for x in mat[i] if x == 1]), i))
        heapq.heapify(strength_index_heap)
        output = []
        for _ in range(k):
            output.append(heapq.heappop(strength_index_heap)[1])
        #print(strength_index_heap)
        return output
    
# approach 2: using list and sort

# time O(m.n + mlogm)
# space O(m)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength_list = [(sum(row), i) for i, row in enumerate(mat)]
        strength_list.sort()
        return [i for strength, i in strength_list[:k]]
    
# approach 3: using binary search and priority queue

# time O(mlogn + mlogk)
# space O(k)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        def binary_search(row):
            left, right = 0, len(row)
            while left < right:
                mid = (left + right) / 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid 
            return left

        pq = []
        for i, row in enumerate(mat):
            strength = binary_search(row)
            entry = -strength, -i
            if len(pq) < k or entry > pq[0]:
                heapq.heappush(pq, entry)
            if len(pq) > k:
                heapq.heappop(pq)
        # print(pq) [(-2, -3), (-2, 0), (-1, -2)]
        output_of_indexes = []
        while pq:
            output_of_indexes.append(-heapq.heappop[1])
        # print(output_of_indexes) [3, 0, 2]
        return output_of_indexes[::-1]

        

        
            
        
            

            