class Solution:
    """Approach 1: Using a list to store 3 maximum elements. 
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 44 ms
       Memory: 14.7 MB"""
    def thirdMax(self, nums):
        v = [float('-inf')]*3
        for num in nums:
            if num not in v:
                if num > v[0]:
                    v = [num, v[0], v[1]]
                elif num > v[1]:
                    v = [v[0], num, v[1]]
                elif num > v[2]:
                    v = [v[0], v[1], num]
        return max(nums) if float('-inf') in v else v[2]

def main():
    numbers =[3, 2, 1]
    s=Solution()
    print(s.thirdMax(numbers))
    numbers = [1, 2]
    print(s.thirdMax(numbers))
    numbers = [2, 2, 3, 1]
    print(s.thirdMax(numbers))
    numbers = [1, 0, 1, 0]
    print(s.thirdMax(numbers))
    numbers = [1, 2, 3, 4, 5, 6]
    print(s.thirdMax(numbers))

if __name__ == '__main__':
    main()

"""if len(nums)<3:
    return max(nums)
   f_max, s_max, t_max = nums[2], nums[1], nums[0]
   for i in range(len(nums)):
       print()
       if n > f_max:
           f_max = n
       elif s_max < n < f_max:
           s_max, t_max = n, s_max
       elif n < f_max and n > t_max:
           t_max = n
    return t_max if t_max < s_max < f_max else f_max"""
