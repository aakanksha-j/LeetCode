# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
"""Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.

Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.
"""

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

# testcase 6*6 matrix [[1, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1]]
# answer 3

"""
        # everyone must know celebrity
        # celebrity must know no one
        i = 0
        for j in range(1, n):
            #print(i,j)
            if knows(i, j) and not knows(j, i):
                i = j
                    
        for j in range(n):
            if i == j: continue
            if knows(i, j) or not knows(j, i):
                return -1
                
        return i
                
# own solution: needs caching
# Without cache:
# Runtime complexity:O(n + n) ~ O(n). O(n-1) - iterate over every person to find the candidate, O(n) - to determine they satisfy eligibility conditions.
# Space complexity: O(1)

def findCelebrity(self, n: int) -> int:
        candidate = 0
        i = 1
        while i < n:
            if candidate == i:
                continue
            if knows(candidate, i):
                candidate = i
            i += 1
        for i in range(n):
            if candidate == i:
                continue
            if not knows(i, candidate) or knows(candidate, i):
                return -1
        return candidate

        
# with cache:
# Runtime complexity: O(n) - iterate over every person to find the candidate, O(n) - to determine they satisfy eligibility conditions. O(n + n) ~ O(n)
# Space complexity: O(n) - store calculated results in cache, not worth the extra code as we will anyways need to go over n-1 iterations for worst case
# from functools import cache

class Solution:
    @cache # smaller and faster than lru_cache as there is no need to evict old values
    def cached_knows(self, a, b):
        return knows(a, b)

    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if candidate == i:
                continue
            if self.cached_knows(candidate, i) and not self.cached_knows(i, candidate):
                candidate = i
     
        for j in range(n):
            if candidate == j:
                continue
            if not self.cached_knows(j, candidate) or self.cached_knows(candidate, j):
                return -1
        return candidate
            
        
"""