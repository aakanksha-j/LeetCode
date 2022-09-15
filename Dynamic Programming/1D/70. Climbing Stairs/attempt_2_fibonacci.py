class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0: return 0
        if n<=2: return n
        two_steps_before=1
        one_step_before=2
        all_ways=0
        for i in range(2,n):
            all_ways=one_step_before+two_steps_before
            one_step_before,two_steps_before=all_ways,one_step_before
        return all_ways

s=Solution()
print(s.climbStairs(9))
