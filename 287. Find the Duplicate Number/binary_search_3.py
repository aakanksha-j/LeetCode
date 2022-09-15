class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # binary search solution
        # time: O(nlogn), space: O(1)

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            count = sum(num <= mid for num in nums)
            if count > mid:
                duplicate = mid
                high = mid - 1
            else:
                low = mid + 1

        return duplicate

""" Take a cumulative sum of counts: for eg. [4,2,4,3,1,5,6] is [1,2,3,5,6,7. It
should be ideally [1,2,3,4,5,6] if no duplicates existed. Therefore, the lowest
number where mismatch begins is the duplicate number.

Algorithm:
1. """
