class Solution:
    """Approach 1: If array contains only one element, then return that element.
                   If nums[left] < nums[right] then the array is not rotated or
                   rotated at position 0. If nums[left] = nums[right], either [1,1]
                   or [3,1,3], therefore search the entire array as binary search
                   won't work. For nums[left] > nums[right], use binary search
                   as we know that element is the smallest only when nums[mid] is
                   greater than nums[mid + 1]. If nums[left] is lesser than nums[mid],
                   then smallest element is beyond mid.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 56 ms
       Memory: 15.1 MB
    """
    def search(self, nums) -> int:
        if len(nums) == 1: # list has only one element
            return nums[0]

        left, right = 0, len(nums) - 1

        if nums[left] < nums[right]: # list is not rotated
            return nums[0]

        # = for [1,1], [3,1,3] testcase
        if nums[left] == nums[right]:
            minimum = nums[left]
            while left != right:
                if nums[left] > nums[right]:
                    minimum = nums[right]
                right -= 1
            return minimum

        # we are here means array is rotated, nums[left] > nums[right]
        while left <= right: # = means only 1 element remaining which has to be
                            # the largest element.
            mid = left + (right - left) // 2
            if nums[mid] <= nums[mid + 1]: # = for duplicate elements.
                if nums[left] <= nums[mid]: # = because left could be equal to mid
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return nums[mid + 1]

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
    numbers = [3,1,3] # failed testcase
    print(s.search(numbers))

if __name__ == '__main__':
    main()
