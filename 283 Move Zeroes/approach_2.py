class Solution(object):
    def moveZeroes(self, nums):
        """
        Approach 2: Two pointers, i and z. i represents the point until where
                    elements in nums are non-zero. z represents the point from
                    where elements begin to be 0. Relative order of non-zero
                    elments is not maintained. Output needed is number of
                    non-zero elements in array.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        i=0
        z=len(nums)-1
        while i<z:
            if nums[i]==0:
                if nums[z]!=0:
                    nums[i],nums[z]=nums[z],nums[i]
                    z-=1
                    i+=1
                else:
                    z-=1
            else:
                i+=1
        #print(i,z)
        if nums[i]!=0:
            return i+1
        else:
            return i


s=Solution()
B=[1,3,2,6,5,0,0,0,0]
print(s.moveZeroes(B)) # output=5
