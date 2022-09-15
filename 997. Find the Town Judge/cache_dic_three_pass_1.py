class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if not trust:
            if n == 1: return 1
            if n > 1: return -1

        cache = {i: set() for i in range(1, n+1)}

        # build trust relationships
        for i,j in trust:
            cache[j].add(i)

        # find candidate
        candidate = -1
        for key in cache:
            if len(cache[key]) == n - 1:
                candidate = key

        # ensure candidate does not trust anyone
        for key in cache:
            if len(cache[key]) > 0 and key != candidate and candidate in cache[key]:
                return -1

        return candidate

9 6 2022 997 Find the Town Judge

time O(3N) ~ O(N)
space O(N) for cache dictionary to build relationships
