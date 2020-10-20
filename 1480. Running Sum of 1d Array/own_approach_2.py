class Solution(object):
    def runningSum(self, nums):
        """
        Approach 1: Using usual approach of looping through elements and add.
        Time complexity: O(n) 40 ms
        Space complexity: O(1) 14.3 MB
        """
        output = []
        count = 0
        for n in nums:
            count += n
            output.append(count)
        return output

A=[3,1,2,10,1]
s=Solution()
print(s.runningSum(A)) # output[1,3,12,0,0]
