class Solution:
    """Approach 1: Return index of peak element. Recursive approach.
                   No repetition of values allowed.
       Time complexity: O(log n)
       Space complexity: O(1)
       Runtime: 44 ms
       Memory: 14.5 MB
    """
    def findPeakElement(self, nums) -> int:
        if len(nums) == 1: # [1]
            return nums[0]
        if nums[0] > nums[1]: # [3,1,2]
            return nums[0]
        if nums[-2] < nums[-1]: # [1,2,3]
            return nums[-1]

        def search(nums, left, right):
            mid = left + (right - left) // 2
            print('mid:', mid)
            if left == right:
                return nums[left]
            if nums[mid] > nums[mid + 1]:
                return search(nums, left, mid)
            else:
                return search(nums, mid + 1, right)

        return search(nums, 1, len(nums) - 2)

def main():
    numbers = [16,17,18,16]
    s=Solution()
    print(s.findPeakElement(numbers))
    numbers =[16, 15, 14, 13]
    print(s.findPeakElement(numbers))
    numbers =[16,18,16,1,2,3,0]
    print(s.findPeakElement(numbers))

if __name__ == '__main__':
    main()
