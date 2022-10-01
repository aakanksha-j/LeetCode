class Solution:
    def reverseWords(self, s: str) -> str:
        # split the string when we come across space and append each word to list
        # append each word in reverse order to output string
        
        # time: O(M.n) - M - no of words, N - length of word
        # space: O(M) - list of words
        
        output = ''
        word_list = s.split(' ')
        #print(word_list)
        for j, word in enumerate(word_list):
            if output != '':
                output += ' '
            n = len(word)
            for i in range(n-1, -1, -1):
                output += word[i]
        return output
            