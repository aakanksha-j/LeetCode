class Solution:
    """Approach 2: Revised Binary Search. No need to find pivot. Divide array
                   into 2 types of sections based on whether nums[left] <= nums[mid].
                   Based on location of target, this will further bifurcate each
                   of the two sections in two quadrants. Return location of
                   target based on those 4 conditions.
       Time complexity: O(log n)
       Space complexity: O(1)
       Runtime: 44 ms
       Memory: 14.7 MB
    """
    def search(self, nums, target: int) -> int:
        print(nums, target)

        left = 0
        right = len(nums) - 1

        while left <= right: # using template 1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: # = for scenario [3,1] target = 1
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1 # element not found in either arrays.

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
    numbers = [4,5,7,8,9,10,11,12,13,14,15,17,1,2,3]
    target = 16
    print(s.search(numbers, target))
    numbers = [3, 1]
    target = 3
    print(s.search(numbers, target))
    """
    """

if __name__ == '__main__':
    main()
