class Solution:
    """Approach 1: Binary search Template 1. If length of array is 1 then check
                   whether that element is target. Find pivot using binary search.
                   Use pivot to check for edge cases. Check if nums[pivot] is
                   equal to target. If nums[left] < nums[right], pivot is 0,
                   array is not rotated and therefore search entire array. Based
                   on whether nums[left] < target or not, use binary search again
                   to find target location in respective sections.
       Time complexity: O(log n)
       Space complexity: O(1)
       Runtime: 44 ms
       Memory: 14.8 MB
    """
    def search(self, nums, target: int) -> int:
        #print(nums, target)
        def find_pivot(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < nums[mid + 1]: # 7 < 8. 8 is not the smallest element.
                    if nums[left] <= nums[mid]: # = because left could be equal to mid
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    return mid + 1

        def binary_search_2(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if target == nums[mid]:
                    return mid
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        pivot = find_pivot(0, len(nums) - 1)
        #print('pivot:', pivot)
        if nums[pivot] == target:
            return pivot
        if pivot == 0: # if array is not rotated, search in entire array
            return binary_search_2(0, len(nums) - 1)
        if nums[0] <= target: # target is in left array. # = because [3,1], 3 scenario failed
            return binary_search_2(0, pivot)
        # target is in right array.
        return binary_search_2(pivot, len(nums) - 1)


def main():
    s=Solution()
    numbers = [1,2,3,4,5]
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
    print(s.search(numbers, target))

if __name__ == '__main__':
    main()
