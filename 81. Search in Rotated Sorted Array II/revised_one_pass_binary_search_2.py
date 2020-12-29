class Solution:
    """Approach 2: Use one pass binary solution used in Search in RSA without
                   duplicates and for nums[left] = nums[mid] condition, increase
                   value of left by 1. Alternatively, we can decrease value of
                   right by 1 by comparing nums[mid] and nums[right]. 
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 52 ms
       Memory: 15 MB
    """
    def search(self, nums, target: int) -> int:
        print(nums, target)

        left = 0
        right = len(nums) - 1

        while left <= right: # using template 1
            mid = (left + right) // 2
            print('mid:', mid)
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: # nums[left] == nums[mid]
                left += 1 # equivalent of left = mid + 1

        return -1 # element not present

def main():
    s=Solution()
    numbers = []
    target = 2
    print(s.search(numbers, target))
    numbers = [1]
    target = 2
    print(s.search(numbers, target))
    numbers = [1]
    target = 0
    print(s.search(numbers, target))
    numbers = [1]
    target = 1
    print(s.search(numbers, target))
    numbers = [1,3]
    target = 3
    print(s.search(numbers, target))
    numbers = [3,1]
    target = 1
    print(s.search(numbers, target))
    numbers = [1, 1]
    target = 2
    print(s.search(numbers, target))
    numbers = [1,1,1]
    target = 2
    print(s.search(numbers, target))
    numbers = [1,1,3]
    target = 3
    print(s.search(numbers, target))
    numbers = [1,3,1]
    target = 1
    print(s.search(numbers, target))
    numbers = [3,1,1]
    target = 3
    print(s.search(numbers, target))
    numbers = [1,3,5]
    target = 5
    print(s.search(numbers, target))
    numbers = [3,5,1]
    target = 3
    print(s.search(numbers, target))
    numbers = [5,1,3]
    target = 4
    print(s.search(numbers, target))

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
    numbers = [4,5,6,7,0,2,3]
    target = 1
    print(s.search(numbers, target))
    numbers = [4,5,7,8,1,2,3]
    target = 5
    print(s.search(numbers, target))
    numbers = [4,5,7,8,9,10,11,12,13,14,15,17,1,2,3]
    target = 15
    print(s.search(numbers, target))
    numbers = [3,4,1,3,3,3,3]
    target = 4
    print(s.search(numbers, target))


if __name__ == '__main__':
    main()
