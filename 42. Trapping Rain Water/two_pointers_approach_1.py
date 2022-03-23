#https://leetcode.com/problems/trapping-rain-water/discuss/17357/Sharing-my-simple-c%2B%2B-code%3A-O(n)-time-O(1)-space
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxleft, maxright = 0, 0
        res = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxleft:
                    maxleft = height[left]
                else:
                    res += maxleft - height[left]
                left += 1
            else:
                if height[right] >= maxright:
                    maxright = height[right]
                else:
                    res += maxright - height[right]
                right -= 1
        return res

"""time: O(n)
space: O(1)
water is trapped when maxright/maxleft is greater than current max and curr
height is less than current max's height.
for example [3,0,3], maxright is 3 and maxleft is 3, current left height is 0
which is less than maxleft, so we add to result maxleft-height[left] = 3 and res
is 3. """
