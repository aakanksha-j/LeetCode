class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # why solving using DP? asked maximum of something, answer of current depends on previous' solution

        # 2 solutions: 1. neetcode - using 2 for loops, 2. intelligently build subsequence
        # both have O(n^2) time complexity because of 2 for loops
        # space required is O(n) to store cache LIS array.

        """# solution 1 - neetcode
        # initialize LIS array which serves as cache for DP solution
        # i - we start from last element and iterate to the first one. (first for loop)
        # j - to compare, we create another for loop, which starts from the next of i element and goes to the last element
        # default value of every element of LIS is 1
        # if value at i is less than value at j,
        # take max of (1 + values returned by j for loop), ith location's value
        # append this value for ith location in LIS array
        # return max value of LIS array

        # test case: [1,2,4,3]
        LIS = [1] * len(nums) # cache for DP solution - array contains longest subsequence for that location eg. nums: 3,LIS[3] = 1, nums:4, LIS[2] = 1, nums:2,LIS[1] = 2, nums:1, LIS[0] = 3

        for i in range(len(nums)-1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j]) # index out of range not faced because LIS array declared with len(nums) elements

        return max(LIS)"""

        """# solution 2 - intelligently build a subsequence from leetcode solution
        # create LIS array with 1st element of nums
        # iterate nums array from 2nd element
        # append element whenever element with greater than last LIS value is found
        # replace whenever element is smaller than last LIS value as rest of array may contain elements greater than element and lesser than last LIS value
        # way to append - iterate LIS array, find the first element greater than current value and replace
        # return length of LIS array
        # eg. [3,4,5,1] LIS = [3,4,5] then becomes [1,4,5]

        LIS = [nums[0]]

        for num in nums:
            if num > LIS[-1]: # No index out of range as 1st element added in LIS
                LIS.append(num)
            else: # find first element in LIS greater than or equal to num
                i = 0
                while num > LIS[i]:
                    i += 1
                LIS[i] = num

        return len(LIS)"""

        # intelligently building subsequence above optimized for performance
        # LIS in above answer is sorted, so instead of linear, binary search can be done
        # time reduces from O(n^2) to O(N.LogN),
        # space stays same O(N), if entire input is increasing, len(LIS) == len(nums)
        LIS = []

        for num in nums:
            i = bisect_left(LIS, num)

            # if num is greater than any element in LIS
            if i == len(LIS):
                LIS.append(num)
            # otherwise, replace the first element encountered in sub greater than or equal to num
            else:
                LIS[i] = num

        return len(LIS)
