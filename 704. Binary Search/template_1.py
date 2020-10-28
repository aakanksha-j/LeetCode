class Solution:
    """Approach 1:
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 224 ms
       Memory: 15 MB"""
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + ((right-left)//2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

def main():
    numbers = [-1,0,3,5,9,12]
    target = 9
    s=Solution()
    print(s.search(numbers, target))
    numbers = [-1,0,3,5,9,12]
    target = 2
    print(s.search(numbers, target))


if __name__ == '__main__':
    main()
