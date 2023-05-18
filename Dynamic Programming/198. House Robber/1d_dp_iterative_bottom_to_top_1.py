class Solution:
    def rob(self, nums: List[int]) -> int:
        # similar to min cost climbing stairs - 1D DP
        
        # time: O(N)
        # space: O(1)
        
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums)
        if n == 3: return max(nums[0] + nums[2], nums[1])
        
        o1, o2, o3 = nums[0], nums[1], nums[0] + nums[2]
        for i in range(3, n):
            output = nums[i] + max(o1, o2)
            o1, o2, o3 = o2, o3, output
            
        return max(o1, o2, o3)
        

class Solution:
    def rob(self, nums: List[int]) -> int:
        last_to_last, last = 0, 0
        for num in nums: 
            last_to_last, last = last, max(last_to_last + num, last)
        return last