class Solution:
    """Approach 1: Binary search Template 3. https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14699/Clean-iterative-solution-with-two-binary-searches-(with-explanation)
       Time complexity: O(log n)
       Space complexity: O(1)
       Runtime: 84 ms
       Memory: 15.3 MB
    """
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def search(self, nums, target: int):
        left_idx = self.extreme_insertion_index(nums, target, True)

        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]

def main():
    s=Solution()
    numbers = [1,2,3,4,5]
    target = 2
    print(s.search(numbers, target))
    numbers = [5,7,7,8,8,10]
    target = 8
    print(s.search(numbers, target))
    numbers = [5,7,7,8,8,10]
    target = 6
    print(s.search(numbers, target))
    numbers = [6,6,6,6]
    target = 6
    print(s.search(numbers, target))
    numbers = [1,1,2,2,2]
    target = 2
    print(s.search(numbers, target))
    numbers = [2,2,2,3,3]
    target = 2
    print(s.search(numbers, target))
    numbers = [0,0,1,2,2]
    target = 1
    print(s.search(numbers, target))
    numbers = [1,2,2,3,3]
    target = 2
    print(s.search(numbers, target))
    numbers = [1,1,2,2,3]
    target = 2
    print(s.search(numbers, target))
    numbers = [2,2,2,3,3,3,4]
    target = 2
    print(s.search(numbers, target))
    numbers = [4,5,7,8,9,10,11,12,13,17,17,17,17]
    target = 17
    print(s.search(numbers, target))
    numbers = [1,2,3,3,3,3,3,4,5,9]
    target = 3
    print(s.search(numbers, target))

if __name__ == '__main__':
    main()
