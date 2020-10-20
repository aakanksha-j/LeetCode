class Solution(object):
    def runningSum(self, nums):
        """
        Approach 1: Using enumerate to index and add giving cumulative sum.
                    Modification of input list is allowed or not is not
                    mentioned. Therefore, assumed extra space for output.
        Time complexity: O(n) 40 ms
        Space complexity: O(1) 14.4 MB
        """
        output = [nums[0]]
        for idx, n in enumerate(nums[1:], 1):
            output.append(output[idx - 1] + n)
        return output

A=[3,1,2,10,1]
s=Solution()
print(s.runningSum(A)) # output[1,3,12,0,0]
