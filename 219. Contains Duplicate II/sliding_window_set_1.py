class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        left = 0
        for right, n in enumerate(nums):
            if n in seen:
                return True
            seen.add(n)
            if len(seen) > k:
                seen.remove(nums[right - k])
        return False

"""
# Using dictionary, instead of set
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # using dictionary and sliding window

        # we save the latest location of element in dictionary
        # irrespective of element is already present or not
        # that way, if the same element is present twice,
        # we will only consider the occurence closest to k distance

        seen = {}
        i = 0
        for j in range(len(nums)):
            if nums[j] in seen and j - seen[nums[j]] <= k:
                return True
            seen[nums[j]] = j

        return False
"""
