class Solution:
    """Approach 2: Template 1
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 44 ms
       Memory: 14.2 MB"""
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif x < mid**2:
                r = mid - 1
            else:
                l = mid + 1

def main():
    numbers = 436451335
    s=Solution()
    print(s.mySqrt(numbers))
    numbers = 82
    print(s.mySqrt(numbers))
    numbers = 15
    print(s.mySqrt(numbers))

if __name__ == '__main__':
    main()
