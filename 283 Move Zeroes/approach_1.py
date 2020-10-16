class Solution(object):
    def moveZeroes(self, nums):
        """
        Approach 1: Two pointers, i and z. z traverses entire array.
                    i moves only when nums[i] is not zero. If nums[i] is 0 and
                    nums[z] is not, then swap since i will always be less than z.
                    Relative order of non-zero elements is maintained. Output
                    needed is modified array.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        i=0
        z=i+1
        while i<z and z<len(nums):
            #print(i,z)
            if nums[i]==0:
                if nums[z]!=0:
                    nums[i],nums[z]=nums[z],nums[i]
                    i+=1
            else:
                i+=1
            z+=1
        return nums

A=[]
s=Solution()
print(s.moveZeroes(A)) # output[1,3,12,0,0]
