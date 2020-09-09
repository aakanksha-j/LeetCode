class Solution:
    def removeDuplicates(self, nums):
        if len(nums)<2: return len(nums)
        k=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
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
