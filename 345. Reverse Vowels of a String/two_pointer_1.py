class Solution:
    """Approach 1: Use two pointers i and j to traverse the string. Similar to
                   sort array by parity solution.
       Time complexity: O(n) 1 while loop
       Space complexity: O(n) for another string
       Runtime: 180 ms for vowel string and 188 ms for vowel list
       Memory: 15.1 MB for vowel string and 14.8 MB for vowel list"""
    def reverseVowels(self, s):
        i = 0
        j = len(s) - 1
        l = 'aeiouAEIOU'
        rs = s[:]
        while i < j:
            if s[i] in l and s[j] in l: # swap when both are vowels
                rs = rs[:i] + s[j] + rs[i+1:j] + s[i] + rs[j+1:]
                i += 1
                j -= 1
            if s[i] not in l: # increase when alphabet is not vowel
                i += 1
            if s[j] not in l: # devrease when alphabet is not vowel
                j -= 1
        return rs

def main():
    p=Solution()
    s='hello'
    print(p.reverseVowels(s))
    s='aA'
    print(p.reverseVowels(s))
    s='aeiou'
    print(p.reverseVowels(s))
    s='ctcgrgtch'
    print(p.reverseVowels(s))

if __name__ == '__main__':
    main()
