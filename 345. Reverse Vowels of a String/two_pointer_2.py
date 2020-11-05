class Solution:
    """Approach 2: Convert string to list and then swap as an array.
       Time complexity: O(n) 1 while loop
       Space complexity: O(n) for another string
       Runtime: 40 ms for vowel string and 64 ms for vowel list
       Memory: 14.9 MB for vowel string and 14.7 MB for vowel list"""
    def reverseVowels(self, s):
        i = 0
        j = len(s) - 1
        l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        rs = list(s)
        while i < j:
            if s[i] in l and s[j] in l: # swap when both are vowels
                rs[i], rs[j] = rs[j], rs[i]
                i += 1
                j -= 1
            if s[i] not in l: # increase when alphabet is not vowel
                i += 1
            if s[j] not in l: # devrease when alphabet is not vowel
                j -= 1
        return ''.join(rs)

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
