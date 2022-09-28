class Solution:
    def maxSubArray(self, nums: List[int]) -> int:\
        # neetcode solution

        maxsum = nums[0]
        cursum = 0

        for n in nums:
            if cursum < 0:
                cursum = 0
            cursum += n
            maxsum = max(maxsum, cursum)

        return maxsum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  
        # own approach
        max_sum = nums[0]
        cur_sum = 0
        
        for n in nums:
            cur_sum = max(cur_sum + n, n)
            max_sum = max(max_sum, cur_sum)
        
        return max_sum
         
            
        
TestCase
1. [2,3,-2,4]
2. [-2,0,-1]
3. [-2,1,-3,4,-1,2,1,-5,4]
4. [5,4,-1,7,8]
5. [1]