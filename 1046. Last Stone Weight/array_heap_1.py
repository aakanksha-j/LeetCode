"""
1046. Last Stone Weight
Easy
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1
 

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""

# heap approach 
# O(nlogn) time - converting array to heap takes O(n) time
# we do two pop and one optional push operation n times i.e logn time - total nlogn
# O(n) or O(logn) space

import heapq
from typing import List

# https://leetcode.com/problems/last-stone-weight/discuss/294956/JavaC%2B%2BPython-Priority-Queue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            print(h)
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
            print(h)
        return -h[0]
    

import bisect

# using array 
def lastStoneWeight(self, stones):
        output = stones[:]
        output.sort()
        while len(output) > 1:
            #print(output)
            bisect.insort(output, output.pop() - output.pop())
        return output[0]

# own solution using array
def lastStoneWeight(self, stones: List[int]) -> int:
        output = stones[:]
        output.sort()
        while len(output) > 1:
            temp = output[-1] - output[-2]
            output.pop()
            output.pop()
            if temp > 0:
                output.append(temp)
                output.sort()
        return 0 if len(output) == 0 else output[-1]
        
# O(n^2) time for array solution as we sort inside while loop
# O(n) space 