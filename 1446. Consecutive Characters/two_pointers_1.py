class Solution:
    """Approach 1: Two variables i and j and while loop used to iterate through
                   entire string. 
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 224 ms
       Memory: 15 MB"""

    def maxPower(self, s):
        i = 0
        j = i + 1
        count = temp_count = 1
        temp_char = s[i]
        while j < len(s):
            if s[i] == s[j]:
                temp_count += 1
            else:
                temp_count = 1
            if temp_count > count:
                count = temp_count
            i += 1
            j += 1
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
