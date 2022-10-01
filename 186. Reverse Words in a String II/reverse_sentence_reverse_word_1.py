class Solution:
    # leetcode solution - reverse the whole string and then reverse each word
    
    # https://leetcode.com/problems/reverse-words-in-a-string-ii/discuss/53832/Python-solution
    
    # time: O(N) - two passes along the string
    # space: O(1) - constant space solution, modified s in-place
    
    def reverse(self, start, end, to_be_reversed):
        while start < end:
            to_be_reversed[start], to_be_reversed[end] = to_be_reversed[end], to_be_reversed[start]
            start += 1
            end -= 1
        
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse the entire sentence
        self.reverse(0, len(s) - 1, s)
        
        # reverse each word
        start = end = 0
        for i in range(len(s)):
            if s[i] == ' ':
                end = i - 1
                self.reverse(start, i - 1, s)
                start = i + 1
            elif i == len(s) - 1:
                self.reverse(start, i, s)
        