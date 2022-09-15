class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window

        # keep moving right by increasing right pointer and count zeroes
        # whenever the count is more than k, 1. check value of nums[left] and
        # 2. decrease count if we are getting rid of zero
        # move left pointer to right
        
        left = 0
        count = 0
        for right in range(len(nums)):
            #print(left, right,count)
            if nums[right] == 0:
                count += 1
            if count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
        return right - left + 1

"""https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC%2B%2BPython-Sliding-Window"""
