class Solution:
    def firstMissingPositive(self, nums):
        i=0
        while i<len(nums):
            print('i:',i)
            if 0<nums[i]<=len(nums) and nums[i]!=i+1 and nums[nums[i]-1]!=nums[i]:
                #swap if number is in range.
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1

def main():
    numbers =  [-1]
    s=Solution()
    print(s.firstMissingPositive(numbers))

if __name__ == '__main__':
    main()
