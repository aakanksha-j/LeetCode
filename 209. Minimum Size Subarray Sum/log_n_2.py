class Solution:
    """Approach 2: Sliding window and two pointers' techniques used
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 68 ms
       Memory: 16.8 MB"""
    def minSubArrayLen(self, s, nums):
        left=total=0
        result=len(nums)+1
        for right, n in enumerate(nums):
            total+=n
            while total>=s:
                result=min(result,right-left+1) # +1 because 0 indexing
                total-=nums[left]
                left+=1
        return result if result<=len(nums) else 0


s = 7 # 15 # 11
nums =[2,3,1,2,4,3] # [5,1,3,5,10,7,4,9,2] # [1,2,3,4,5]
p=Solution()
print(p.minSubArrayLen(s,nums))
