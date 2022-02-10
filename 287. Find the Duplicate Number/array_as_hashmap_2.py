class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Array as hashmap (Iterative)
        # time - O(n), space - O(1)

        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]
