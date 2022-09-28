from unittest import TestCase


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # leetcode solution
        # DP Kadane algorithm - edge case 0 and -ve numbers
        
        # time: O(n)
        # space: O(1)
        
        min_so_far, max_so_far = nums[0], nums[0]
        max_output = max_so_far
        for num in nums[1:]:
            # print('max_so_far', max_so_far)
            # print('min_so_far', min_so_far)
            # print(num, min_so_far * num, max_so_far * num)
            max_so_far, min_so_far = max(num, min_so_far * num, max_so_far * num), min(num, min_so_far * num, max_so_far * num)
            max_output = max(max_output, max_so_far)
            # print('max_output', max_output)
            
        return max_output


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # neetcode solution 
        
        output = max(nums)
        cur_max, cur_min = 1, 1
        
        for num in nums:
            temp = cur_max * num
            cur_max  = max(cur_max * num, num, cur_min * num)
            cur_min = min(temp, num, cur_min * num)
            output = max(output, cur_max)
        
        return output


TestCase
1. [2,3,-2,4]
2. [-2,0,-1]
3. [-2,1,-3,4,-1,2,1,-5,4]
4. [5,4,-1,7,8]
5. [1]