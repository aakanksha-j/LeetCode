"""169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?"""

# Boyer Moore algorithm
# time O(n) space O(1)
# The problem states there must be a majority element; 
# it has to show up >n/2 times NOT just n/2. 
# Something like [1, 1, 1, 1, 2, 3, 4, 5] is an invalid input.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate = num
                count += 1
            else:
                count -= 1
                
        return candidate