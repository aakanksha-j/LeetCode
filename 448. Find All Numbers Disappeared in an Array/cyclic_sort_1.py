class Solution:
    def findDisappearedNumbers(self, nums):
        i=0
        while i<len(nums):
            print('i:',i)
            if 0<nums[i]<=len(nums) and nums[i]!=i+1 and nums[nums[i]-1]!=nums[i]:
                #swap if number is in range.
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            else:
                i+=1
        output=[]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                output.append(i+1)
        return output

def main():
    numbers =[4,3,2,7,8,2,3,9]
    s=Solution()
    print(s.findDisappearedNumbers(numbers))

if __name__ == '__main__':
    main()
