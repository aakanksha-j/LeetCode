class Solution:
    def removeDuplicates(self, nums):
        if len(nums)<2: return len(nums) # Code failed for scenario when len was 1.
        k=1 # to get rid of index out of range error.
        for i in range(1,len(nums)): #  Start looping from 2nd element.
            if nums[i]>nums[i-1]: # Compare with previous element which is already included in k
                nums[k]=nums[i]
                k+=1
        return k

def main():
    numbers = [0,0,1,1,1,2,2,3,3,4]
    s=Solution()
    print(s.removeDuplicates(numbers))
    print(numbers)

if __name__ == '__main__':
    main()
