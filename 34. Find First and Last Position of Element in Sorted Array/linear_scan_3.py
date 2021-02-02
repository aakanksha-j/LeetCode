class Solution:
    """Approach 2: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/
       Time complexity: O(log n)
       Space complexity: O(1)
       Runtime: 112 ms
       Memory: 15.4 MB
    """
    def search(self, nums, target: int):
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]

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
