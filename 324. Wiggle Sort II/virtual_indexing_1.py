"""Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.

 

Example 1:

Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
Example 2:

Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 5000
It is guaranteed that there will be an answer for the given input nums.
 

Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?"""

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        import statistics
        median = statistics.median(nums)
        
        N = len(nums)
        
        map_index = lambda x: (2*x + 1) % (N|1)
        
        left, right = 0, N-1
        current_index = 0
        
        while current_index <= right:
            if nums[map_index(current_index)] > median:
                nums[map_index(current_index)], nums[map_index(left)] = nums[map_index(left)], nums[map_index(current_index)]
                left += 1
                current_index += 1
            elif nums[map_index(current_index)] < median:
                nums[map_index(current_index)], nums[map_index(right)] = nums[map_index(right)], nums[map_index(current_index)]
                right -= 1
            else:
                current_index += 1
            
"""
O(n) time O(1) space virtual indexing
used statistics package to get median
https://leetcode.com/problems/wiggle-sort-ii/discuss/77682/Step-by-step-explanation-of-index-mapping-in-Java
https://leetcode.com/problems/wiggle-sort-ii/discuss/333079/Python-deterministic-O(n)-time-%2B-O(1)-memory-quick-select-%2B-%22median-of-medians%22
https://leetcode.com/problems/wiggle-sort-ii/discuss/77681/O(n)-time-O(1)-space-solution-with-detail-explanations"""