class Solution:
    def tribonacci(self, n: int) -> int:
        tn, tn1, tn2 = 0, 1, 1
        if n == 0: return tn
        if n == 1: return tn1
        if n == 2: return tn2
        curr = 3
        tn3 = 0
        while curr <= n:
            tn3 = tn + tn1 + tn2
            print(tn3)
            print(tn, tn1, tn2)
            tn, tn1, tn2 = tn1, tn2, tn3
            print(tn, tn1, tn2)
            curr += 1
        return tn3

s=Solution()
print(s.tribonacci(4))
print(s.tribonacci(37))
