class Solution:
    """Approach 2: One variable i and for loop used to iterate through entire
                   string. 
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 224 ms
       Memory: 15 MB"""

    def maxPower(self, s):
        count = temp_count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                temp_count += 1
            else:
                temp_count = 1
            if temp_count > count:
                count = temp_count
        return count


def main():
    st = "abbcccddddeeeeedcba"
    s=Solution()
    print(s.maxPower(st))
    st = "ccbccbb"
    print(s.maxPower(st))
    st = "hooraaaaaaaaaaay"
    print(s.maxPower(st))
    st = "tourist"
    print(s.maxPower(st))

if __name__ == '__main__':
    main()
