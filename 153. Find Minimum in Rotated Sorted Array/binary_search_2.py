class Solution:
    """Approach 2: If array contains only one element, then return that element.
                   If nums[left] < nums[right] then the array is not rotated or
                   rotated at position 0. We know that element is the smallest
                   only when nums[mid] is greater than nums[mid + 1]. If nums[left]
                   is lesser than nums[mid], then smallest element is beyond mid.
       Time complexity: O(log n)
       Space complexity: O(1)
       Runtime: 40 ms
       Memory: 14.6 MB
    """
    def search(self, nums) -> int:
        if len(nums) == 1: # list has only one element
            return nums[0]

        left, right = 0, len(nums) - 1

        if nums[left] < nums[right]: # list is not rotated
            return nums[0]

        while left <= right: # = means only 1 element remaining which has to be
                            # the largest element.
            mid = left + (right - left) // 2
            if nums[mid] <= nums[mid + 1]: # = for duplicate elements. [4,0,0,2,3]
                if nums[left] <= nums[mid]: # = because left could be equal to mid
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return nums[mid + 1]

        #return nums[left + 1] # left==right, one element remaining, if 'while left < right:'

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

"""left, right = 0, len(nums) - 1
        while left < right: # using template 2
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]: # [2,3,1], [2,3,3], [4,3,3], [3,3,3]
                left = mid + 1
            else:
                right = mid
        return nums[left]"""
