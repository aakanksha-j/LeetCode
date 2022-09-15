class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # leetcode solution using sort and compare
        temp = nums
        temp.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

"""time: O(nlogn) for sorting and O(n) for linear scan using for loop
space: O(n) for sort() function using timsort algorithm.
We define temp variable because we do not want to modify the input array which is
a requirement mentioned in the question. This solution does not meet the criteria
for using only constant extra space.
Took more than double time as compared to floyd solution. """


        # leetcode solution using set
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

"""time: O(n) for linear scan. Hash set insertion and lookups have amortized
constant space complexities.
space: O(n) to store at most n elements.
This approach too does not use constant space and hence does not meet problem
constraints."""


        # own solution using set
        temp = set()
        for n in nums:
            if n not in temp:
                temp.add(n)
            else:
                return n
