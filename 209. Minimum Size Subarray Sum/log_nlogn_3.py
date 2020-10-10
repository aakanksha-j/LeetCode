class Solution:
    """Approach 3: Binary Search, Sliding window and two pointers' techniques used
       Time complexity: O(n)
       Space complexity: O(1) since original array is modified to get
                         cumulative sum. If inplace not allowed, then O(n)
       Runtime: 128 ms
       Memory: 16.7 MB"""
    def minSubArrayLen(self, s, nums):
        result = len(nums) + 1
        for idx,n in enumerate(nums[1:],1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= s:
                left = self.find_left(left,right,nums,s,n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self,left,right,nums,s,n):
        while left < right:
            mid = left + (right-left) // 2
            if n - nums[mid] >= s:
                left = mid + 1
            else:
                right = mid
        return left

s = 11
nums = [1,2,3,4,5]
p=Solution()
print(p.minSubArrayLen(s,nums))
