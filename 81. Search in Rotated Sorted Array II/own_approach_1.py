class Solution:
    """Approach 1: Binary search Template 1. If length of array is 1 then check
                   whether that element is target.  If nums[left] == nums[right],
                   and nums[left] is not target, then we will search entire array.
                   If nums[left] != nums[right], use one pass revised binary
                   search method learnt in Search in RSA to find target location
                   in respective sections.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 56 ms
       Memory: 15.1 MB
    """
    def search(self, nums, target: int) -> int:
        if len(nums) == 0: # array has no elements
            return -1

        if len(nums) == 1: # array has 1 element
            return nums[0] == target

        left, right = 0, len(nums) - 1

        # search entire array
        if nums[left] == nums[right]:
            if nums[left] == target:
                return left
            while left != right:
                if nums[right] == target:
                    return right
                right -= 1
            return -1

        # binary search similar to without duplicates search in RSA
        while left <= right:
            mid = left + ((right- left) // 2)
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1 # element not present

def main():
    s=Solution()
    """numbers = [1,2,3,4,5]
    target = 2
    print(s.search(numbers, target))
    numbers = [4,5,6,7,0,1,2]
    target = 0
    print(s.search(numbers, target))
    numbers = [4,5,6,7,8,1,2]
    target = 0
    print(s.search(numbers, target))
    numbers = [4,5,6,7,1,2,3]
    target = 6
    print(s.search(numbers, target))
    numbers = [4,5,6,7,1,2,3]
    target = 8
    print(s.search(numbers, target))
    numbers = [4,5,7,8,1,2]
    target = 3
    print(s.search(numbers, target))
    numbers = [1]
    target = 0
    print(s.search(numbers, target))
    numbers = [4,5,6,7,0,2,3]
    target = 1
    print(s.search(numbers, target))
    numbers = [4,5,7,8,1,2,3]
    target = 6
    print(s.search(numbers, target))
    numbers = [3, 1]
    target = 1
    print(s.search(numbers, target))
    numbers = [4,5,7,8,9,10,11,12,13,14,15,17,1,2,3]
    target = 15
    print(s.search(numbers, target))"""
    numbers = [3,3,3,3,3,3,4,5,3]
    target = 5
    print(s.search(numbers, target))

if __name__ == '__main__':
    main()
