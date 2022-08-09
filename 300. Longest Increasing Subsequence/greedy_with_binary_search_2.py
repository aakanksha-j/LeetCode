class Solution:
"""    # dp - https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)

       def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

        O(N^2) time and O(N) space

        # dp solution - O(N^2) time, O(N) space - similar to neetcode

        n = len(nums)
        dp = [1] * n

        for j in range(n):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], 1 + dp[i])

        return max(dp)
        
"""
    # leetcode solution 3 - greedy with binary search

    # time: O(N. log N) - iterate every num in nums and search for location in log N time
    # space: O(N) for lis array

    def binary_search(self, lis, num):
        left, right = 0, len(lis) - 1

        while left < right:
            mid = left + ((right - left) // 2)

            if num == lis[mid]:
                return mid
            elif num < lis[mid]:
                right = mid
            else:
                left = mid + 1

        return left

    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        lis_idx = []
        prev_num_idx = [-1] * len(nums)

        for i, num in enumerate(nums):
            if len(lis) == 0 or lis[-1] < num:
                prev_num_idx[i] = -1 if len(lis_idx) == 0 else lis_idx[-1]
                lis.append(num)
                lis_idx.append(i)

            else:
                idx = self.binary_search(lis, num) # bisect_left(lis, num)
                prev_num_idx[i] = -1 if idx == 0 else lis_idx[idx - 1]
                lis[idx] = num
                lis_idx[idx] = i

        ans = []
        t = lis_idx[-1]
        while t >= 0:
            ans.append(nums[t])
            t = prev_num_idx[t]


        print(lis, lis_idx, prev_num_idx, ans[::-1])
        return len(ans)
