class Solution:
    # leetcode solution - two pointers approach recommended as it can be extended to 3Sum with multiplicity and 3Sum Closest
    # this is similar to two sum approach, two sum II using hashset is possible but not recommended

    # time: O(n^2) - O(nlogn) from sort is lower than n^2 for running i and then finding j and complement
    # space: O(n) or O(logn)

    def two_sum(self, nums, i, output):
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum_of = nums[i] + nums[left] + nums[right]
            if sum_of == 0:
                output.append([nums[i], nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

            elif sum_of > 0:
                right -= 1
            else:
                left += 1


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.two_sum(nums, i, output)
        return output