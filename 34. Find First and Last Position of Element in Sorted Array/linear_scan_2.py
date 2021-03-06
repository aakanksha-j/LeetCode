class Solution:
    """Approach 2: Linear scan using left and right pointers
       Time complexity: O(log n)
       Space complexity: O(1)
       Runtime: 92 ms
       Memory: 15.4 MB
    """
    def search(self, nums, target: int):
        if len(nums) == 0:
            return [-1, -1]
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        left_flag, right_flag = False, False
        while left < right and not (left_flag and right_flag):
            if nums[left] < target:
                left += 1
            elif nums[left] == target:
                left_flag = True
            if nums[right] > target:
                right -= 1
            elif nums[right] == target:
                right_flag = True
        if left_flag or right_flag:
            return [left, right]
        elif left == right and nums[left] == target:
            return [left, left]
        else:
            return [-1, -1]

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
