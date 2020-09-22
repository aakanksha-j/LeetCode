class Solution:
    """Approach 2: Mark the number that index points to as negative and
                   get all th indices with positive number.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 412 ms
       Memory: 21.5 MB"""
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index=abs(nums[i])-1
            nums[index]=-abs(nums[index])
        return [i+1 for i in range(len(nums)) if nums[i]>0]

def main():
    numbers =[4,3,2,7,8,2,3,7]
    s=Solution()
    print(s.findDisappearedNumbers(numbers))

if __name__ == '__main__':
    main()
