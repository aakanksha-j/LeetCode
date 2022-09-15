class Solution:
    """Approach 2: Without using hashset, using cycle detection and fast-slow pointers.
       Time complexity: O(n)
       Space complexity: O(n) for hash set
       Runtime: 36 ms
       Memory: 14.2 MB
    """
    def digit_square_sum(self, n):
        tmp, d_sum = 0, 0
        while n > 0:
            tmp = n % 10
            d_sum += tmp ** 2
            n = n // 10
            print(d_sum)
        return d_sum

    def isHappy(self, n: int) -> bool:
        slow = fast = n
        #print(slow)
        while True:
            slow = self.digit_square_sum(slow)
            print('slow:', slow)
            fast = self.digit_square_sum(self.digit_square_sum(fast))
            #print('fast:', fast)
            if slow == fast:
                return slow == 1

def main():
    s=Solution()
    print(s.isHappy(19))
    print(s.isHappy(362))
    print(s.isHappy(11))

if __name__ == '__main__':
    main()

"""Runtime: 36 ms
Memory: 14.3 MB
set_n = set()
while n != 1:
    n = sum(int(dig)**2 for dig in (str(n)))
    if n in set_n:
        return False
    else:
        set_n.add(n)
    print(set_n)
else:
    return True"""

"""Runtime: 36 ms
Memory: 14.2 MB
seen = set()
while n not in seen:
    seen.add(n)
    n = sum(int(dig)**2 for dig in str(n))
return n == 1"""
