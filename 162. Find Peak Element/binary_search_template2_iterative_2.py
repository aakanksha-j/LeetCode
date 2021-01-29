class Solution:
    """Approach 2: Iterative approach.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 44 ms
       Memory: 14.4 MB
    """
    def findPeakElement(self, nums) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-2] < nums[-1]:
            return len(nums) - 1

        left, right = 1, len(nums) - 2
        while left < right:
            mid = left + (right - left) // 2
            # print('mid:', mid)
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left

def main():
    numbers = [0,2,1,3,0]
    s=Solution()
    print(s.findPeakElement(numbers))
    numbers =[0,3,1,2,0]
    print(s.findPeakElement(numbers))
    numbers =[0,3,2,1,0]
    print(s.findPeakElement(numbers))
    numbers =[0,3,2,1,0]
    print(s.findPeakElement(numbers))

if __name__ == '__main__':
    main()
