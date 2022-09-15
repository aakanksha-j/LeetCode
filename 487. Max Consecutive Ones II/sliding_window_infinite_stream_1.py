class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # sliding window
        # instead of k, only 1 zero can be flipped
        # after 1004. Max Consecutive ones 3, 209. Minimum subarray sum

        result = 0
        left = 0
        lastzeroindex = -1
        for right, n in enumerate(nums):
            if n == 1:
                continue
            else:
                result = max(result, right - left)
                left = lastzeroindex + 1
                lastzeroindex = right
        return max(result, right - left + 1)

"""follow up - infinite stream. maintain left and right pointers, and last seen zero index.
As soon as one encounters 0 in stream, record max length, make left index = last seen zero
index + 1 and set last seen zero index as right. Continue processing the stream."""
    
