# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    """Approach 2: Use ternary search i.e divide into 3 parts. Find 2 mids.
                   Search in one of those 3 parts based on target value.
       Time complexity: O(log3 n)
       Space complexity: O(1)
       Runtime: 24 ms
       Memory: 14.2 MB
    """
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid1 = left + (right - left)//3
            print('mid1:', mid1)
            op1 = guess(mid1)
            if not op1:
                return mid1
            mid2 = right - (right - left)//3
            print('mid2:', mid2)
            op2 = guess(mid2)
            if not op2:
                return mid2
            if op1 < 0: # pick < mid1
                right = mid1 - 1
            elif op2 > 0: # mid1 < pick < mid2
                left = mid2 + 1
            else: # mid2 < pick
                left = mid1 + 1
                right = mid2 - 1
            print('left:', left, 'right:', right)

def main():
    n = 10
    pick = 6
    s=Solution()
    print(s.guessNumber(n))
    n = 20
    pick = 6
    print(s.guessNumber(n))
    n = 30
    pick = 6
    print(s.guessNumber(n))

if __name__ == '__main__':
    main()
