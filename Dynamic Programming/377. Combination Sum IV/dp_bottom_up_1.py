class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # neetcode solution - bottom up dp - dp[target] = sum(dp[target - num]) for num in nums

        # remember 112 and 211 are counted as 2 different combinations
        # we can resuse same number infinite times - Unbounded knapsack

        # time: O(m.n) - m is size of array nums and n is size of target
        # space: O(m.n) - for cache

        # instead of hashmap, using list for cache and doing early optimizations

        dp = [1] + [0] * target # target = 4, nums = [4] then base case dp[4] = dp[target - num] = dp[4-4] = dp[0] = 1
        nums.sort()

        for comb_sum in range(1, target + 1): # since we run from 0 to n, therefore size is n+1,
            # start from 1 is important, otherwise everything becomes 0
            for num in nums:
                if comb_sum >= num:
                    dp[comb_sum] += dp[comb_sum - num]
                else:
                    break

        return dp[target]



class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp - bottom up solution with memoization and optimizations

        # time complexity: O(T.N) - T numbers from 0 to target
        #                         - N numbers from list nums
        # space complexity: O(Nlogn) - sorting nums array for optimization
        #                   O(T) - extra space to store array elements from 0 to T

        # https://leetcode.com/problems/combination-sum-iv/discuss/85120/C%2B%2B-template-for-ALL-Combination-Problem-Set

        # comb[target] += U(comb[target - num])
        # dp[0] = 1 [0], dp[1] = 1 [1]
        # dp[2] = dp[0] + dp[1] = 2 [1, 1], [2]
        # dp[3] = dp[0] + dp[1] + dp[2] = 4 [1,1,1], [1,2], [2,1], [3]
        # dp[4] = dp[0] + dp[1] + dp[2] + dp[3] = 7

        cache = [0]* (target + 1) # need to create array only from 0 to target
        cache[0] = 1 # dp[0] = 1
        nums.sort() # optimization

        # run for loop upto (target + 1) to get dp[comb_n]
        for comb_sum in range(target + 1):
            # run for loop for elements in list nums with value < target
            for num in nums:
                #print(comb_sum, num)
                if comb_sum >= num:
                    cache[comb_sum] += cache[comb_sum - num]
                else: # optimization, early stopping
                    break

                #print(cache)
        return cache[target]

# if nums = [1,2] and target = 4, since 3 is not included, dp[3] does not
# contain [3], therefore dp[4] will not contain [1,3], [3,1] permutations.
# Therefore, instead of 7, only 5 combinations are possible. However, dp[3]
# still contains combinations excluding [3] such as [1,2], [2,1], [1,1,1].
# And when dp[4] calls for adding, 1 and 2 get added to these 3 combinations until comb_sum > num
