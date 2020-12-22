# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    """Approach 1: Binary Search Template 1. Guess API gives inverted results as
                   opposed to usual template wherein if nums[mid] < target then
                   -1 should be returned but here if mid < pick, then 1 is
                   returned.
       Time complexity: O(log2 n)
       Space complexity: O(1)
       Runtime: 32 ms
       Memory: 14.2 MB
    """
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            op = guess(mid)
            if op == 0:
                return mid
            elif op == -1: # pick < num (pick = 2, num = 5)
                right = mid - 1
            else:
                left = mid + 1 # pick > num (pick = 6, num = 5, op = 1)

def main():
    n = 200000
    pick = 6
    s=Solution()
    print(s.guessNumber(n))
    n = 2
    pick = 2
    print(s.guessNumber(n))
    n = 2
    pick = 1
    print(s.guessNumber(n))

if __name__ == '__main__':
    main()
