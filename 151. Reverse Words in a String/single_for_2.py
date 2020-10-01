class Solution:
    """Approach 2: Use single for loop to traverse the string and store word in
                   a temporary string and concatenate with output string when
                   space appears.
       Time complexity: O(n)
       Space complexity: O(n)
       Runtime: 44 ms
       Memory: 14.3 MB"""
    def reverseWords(self, s):
        if len(s)==1 and s[0]!=' ':
            return s
        output_string=''
        word=''
        last_letter=''
        for i in range(len(s)):
            if s[i]!=' ':
                if last_letter==' ':
                    output_string=word+' '+output_string
                    word=s[i]
                else:
                    word+=s[i]
            # word contains some letters when we reach end of string and we
            # need to concatenate but concatenation takes place when we reach
            # a letter after blank space, therefore, we will forcibly add
            # letters in word to output_string.
            if i==len(s)-1:
                output_string=word+' '+output_string
            last_letter=s[i]
        return output_string.rstrip()

def main():
    p=Solution()
    s='asdasd df f' #failed here
    print(p.reverseWords(s))
    s='word1 word2'
    print(p.reverseWords(s))
    s=' word1 word2 '
    print(p.reverseWords(s))
    s='  w b'
    print(p.reverseWords(s))
    s='b w  '
    print(p.reverseWords(s))
    s=' w '
    print(p.reverseWords(s))
    s='a b c d'
    print(p.reverseWords(s))

if __name__ == '__main__':
    main()
