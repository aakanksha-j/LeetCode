class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # https://leetcode.com/problems/increasing-triplet-subsequence/discuss/79004/Concise-Java-solution-with-comments.
        
        # linear scan
        # time O(n)
        # space O(1)
        
        n = len(nums)
        if n < 3: return False
        
        first = second = math.inf
        
        for num in nums:
            if num <= first: first = num
            elif num <= second: second = num
            else: return True
            
        return False
        