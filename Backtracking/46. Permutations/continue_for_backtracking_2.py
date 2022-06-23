class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # discuss solution - https://leetcode.com/problems/permutations/discuss/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning)

        res, perm = [], []

        def dfs_backtrack(start = 0):

            # base case:
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i, num in enumerate(nums):
                if num in perm: # already exists in permutation, need not add again
                    continue

                perm.append(num)

                dfs_backtrack(i + 1)

                perm.pop()

        dfs_backtrack()

        return res
