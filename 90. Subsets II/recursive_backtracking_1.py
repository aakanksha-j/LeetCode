class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # leetcode comments solution, backtracking dfs recursive

        # time complexity: O(N.2^N) as for subset either keep or skip that number - 2^N,
        #                  to store subset of len(nums), we need N
        # space complexity: O(N) for recursion call stack

        # similar to 77 combinations sum,
        # instead of stopping only when length of subset == len(nums)
        # add subset to result at every iteration
        # use for loop, continue when same element repeated
        # sorting is required to skip using the same number again

        nums.sort()

        res = []

        def dfs_backtrack(start = 0, subset = []):

            res.append(subset.copy())

            for i in range(start, len(nums)):

                # we cannot reuse number at this position or same previous permutation
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i]) # add
                dfs_backtrack(i + 1, subset) # backtrack
                subset.pop() # remove

        dfs_backtrack()

        return res
