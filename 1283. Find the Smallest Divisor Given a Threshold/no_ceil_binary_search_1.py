class Solution:
    """Approach 1: Binary search Template 2 and calculate sum using separate function.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 388 ms
       Memory: 19.9 MB"""

    def smallestDivisor(self, nums, threshold):
        left = 1
        right = max(nums)
        sum_of_l = sum(num for num in nums)
        if sum_of_l == threshold:
            return left
        #sum_of_r = self.sum_of_nums(right, nums) not needed because sum of
        # threshold is always less than threshold because it is guaranteed that
        # there will be an answer.
        while left < right: # in example 1, l=4,r=5,mid=5 if left<=right,then infinite loop
            mid = left + (right-left) // 2
            sum_of_mid = self.sum_of_nums(mid, nums)
            if sum_of_mid > threshold: # mid increases, sum of mid decreases
                left = mid + 1
            else:
                right = mid
        return mid+1 if sum_of_mid > threshold else mid

    def sum_of_nums(self, mid, nums):
        sum = 0
        for num in nums:
            if num < mid: # 2/3 = 1 rounded to nearest integer
                sum += 1
            elif num%mid == 0: # 3/3 = 1
                sum += num//mid
            else:  # 4/3 = 2 rounded to nearest integer
                sum += num//mid + 1
        return sum


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
