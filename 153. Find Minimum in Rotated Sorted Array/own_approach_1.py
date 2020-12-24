class Solution:
    """Approach 1: Binary search Template 1. If length of array is 1 then return
                   the element. Find pivot using binary search. Return the element
                   at pivot. Used Solution of Search in rotated array.
       Time complexity: O(log n)
       Space complexity: O(1)
       Runtime: 40 ms
       Memory: 14.7 MB
    """
    def search(self, nums) -> int:
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

        if len(nums) == 1:
            return nums[0]
        if len(nums) > 1:
            pivot = find_pivot(0, len(nums) - 1)
            # print('pivot:', pivot)
            return nums[pivot]

def main():
    s=Solution()
    numbers = [1,2,3,4,5]
    print(s.search(numbers))
    numbers = [1]
    print(s.search(numbers))
    numbers = [4,5,6,7,0,2,3]
    print(s.search(numbers))
    numbers = [3, 1]
    print(s.search(numbers))
    numbers = [4,5,7,8,9,10,11,12,13,14,15,17,1,2,3]
    print(s.search(numbers))

if __name__ == '__main__':
    main()
