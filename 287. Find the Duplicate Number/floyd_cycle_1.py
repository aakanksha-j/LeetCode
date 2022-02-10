class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Tortoise and hare Cycle detection algorithm
        # time: O(n) space: O(1)

        fast = slow = nums[0]
        while fast and fast.next:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                slow2 = nums[0]
                while slow != slow2:
                    slow = nums[slow]
                    slow2 = nums[slow2]
                return slow2
