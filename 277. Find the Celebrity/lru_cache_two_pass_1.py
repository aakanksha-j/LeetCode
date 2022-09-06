# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
from functools import lru_cache
class Solution:
    @lru_cache(maxsize = None)
    def cached_knows(self, a, b):
        return knows(a, b)

    def findCelebrity(self, n: int) -> int:
        # two pass - leetcode solution 3
        # time complexity - O(N)
        # space complexity - O(N)

        i = 0
        for j in range(1, n):
            if self.cached_knows(i, j):
                i = j


        for j in range(n):
            if i == j: continue
            if self.cached_knows(i, j) or not self.cached_knows(j, i):
                return -1

        return i
