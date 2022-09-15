class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # neetcode solution - backtracking

        # time: k.nCk - k for appending built combination of length k to output
        #      nCk (n!/(n-k)!k!) from combinations formula, will have to build
        #      these many combinations using recursion
        # space: nCk to store output res

        res = []

        def backtrack(start, comb):
            # base case
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(start, n + 1):
                comb.append(i)

                backtrack(i + 1, comb)

                comb.pop()

        backtrack(1, [])

        return res
