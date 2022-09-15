class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # sliding window

        # similar to 1004. Max consecutive ones 3
        # instead of k, here only 1 zero can be flipped

        # keep moving right pointer
        # count the no. of zeroes
        # whenever count exceeds allowed limit, move left pointer forward
        # before moving left pointer forward, make sure count is adjusted
        # in case, left pointer value was 0, decrease count.

        left = 0
        count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            if count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1

        return right - left + 1
