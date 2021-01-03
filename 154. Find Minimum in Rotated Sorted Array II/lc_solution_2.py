class Solution:
    """Approach 2: Use binary search template 2. Compare nums[mid] and nums[right].
                   Since duplicates are allowed, if nums[mid] = nums[right],
                   decrease value of right by 1. Otherwise, similar to 153.
       Time complexity: O(log n)
       Space complexity: O(1)
       Runtime: 56 ms
       Memory: 15 MB
    """
    def search(self, nums) -> int:
        left, right = 0, len(nums) - 1
        while left < right: # using template 2
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]: # [1,2,3]
                right = mid
            elif nums[mid] > nums[right]: # [2,3,1]
                left = mid + 1
            else:
                right -= 1 # [2,3,3], [4,3,3], [3,3,3]
        return nums[left]

def main():
    s=Solution()
    numbers = [7,0,2,3,4,5,6]
    print(s.search(numbers))
    numbers = [4,5,7,8,9,10,11,12,13,14,15,17,1,2,3]
    print(s.search(numbers))
    numbers = [1,2,3,4,5]
    print(s.search(numbers))
    numbers = [1]
    print(s.search(numbers))
    numbers = [3,1]
    print(s.search(numbers))
    numbers = [4,3,3]
    print(s.search(numbers))
    numbers = []
    print(s.search(numbers))

if __name__ == '__main__':
    main()
