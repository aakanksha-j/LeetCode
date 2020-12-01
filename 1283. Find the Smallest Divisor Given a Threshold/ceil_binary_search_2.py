import math
class Solution:
    """Approach 2: Binary search Template 2 and ceil function
       Time complexity: O(N log Nmax)
       Space complexity: O(1)
       Runtime: 412 ms
       Memory: 20.4 MB"""

    def smallestDivisor(self, nums, threshold):
        compute_sum = lambda x: sum(math.ceil(n/x ) for n in nums)

        left = 1
        right = max(nums)

        if compute_sum(left) <= threshold:
            return left

        while left < right: # in example 1, l=4,r=5,mid=5 if left<=right,then infinite loop
            mid = (left + right) >> 1 # left + (right-left)//2
            if compute_sum(mid) > threshold: # mid increases, sum of mid decreases
                left = mid + 1
            else:
                right = mid
        return left

def main():
    numbers = [1,2,5,9]
    threshold = 6
    s=Solution()
    print(s.smallestDivisor(numbers, threshold))
    numbers = [2,3,5,7,11]
    threshold = 11
    print(s.smallestDivisor(numbers, threshold))
    numbers = [19]
    threshold = 5
    print(s.smallestDivisor(numbers, threshold))
    numbers = [6]
    threshold = 6 # smallestDivisor is 1
    print(s.smallestDivisor(numbers, threshold))
    numbers = [1000000]
    threshold = 6 # smallestDivisor is 1
    print(s.smallestDivisor(numbers, threshold))

if __name__ == '__main__':
    main()
