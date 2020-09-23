class Solution:
    """Approach 3: Mark the number that element points to as negative and
                   get all th indices with positive number.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 444 ms
       Memory: 21.4 MB"""
    def findDisappearedNumbers(self, nums):
        for n in nums:
            index=abs(n)-1
            if nums[index]>0:
                nums[index]*=-1
        return [i+1 for i in range(len(nums)) if nums[i]>0]

def main():
    numbers =[4,3,2,7,8,2,3,7]
    s=Solution()
    print(s.findDisappearedNumbers(numbers))

if __name__ == '__main__':
    main()
