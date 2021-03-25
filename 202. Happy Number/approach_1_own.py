class Solution:
    """Approach 1:
       Time complexity: O(n)
       Space complexity: O(n) for hash set
       Runtime: 48 ms
       Memory: 14.3 MB
    """
    def isHappy(self, n: int) -> bool:
        n_len = len(str(n))
        set_n = set()
        while n not in set_n:
            set_n.add(n)
            n = sum(int(dig)**2 for dig in (str(n)))
            n_len = len(str(n))
            print(set_n)
        return 1 in set_n # or n == 1

def main():
    s=Solution()
    print(s.isHappy(106))
    print(s.isHappy(362))
    print(s.isHappy(11))

if __name__ == '__main__':
    main()
