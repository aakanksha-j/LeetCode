""""
Example:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]"""

"""Approach: Two methods, one to count words in every line and second to fill spaces between words.
Run while loop until words exist in list
3 cases in adding space: 
1. only one word in line, add space, return that word.
2. last line, add one space between each word and return left justified
3. evenly distribute spaces by appending space to each word except last word
"""

"""
Time complexity: O(n) for add_words method and O(2n) for add_space method
Space complexity: O(n) for add_space method for word_space_list"""

class Solution:
    def add_words(self, start_index, maxWidth, words):
        filled_spaces = 0
        end_index = start_index - 1
        i = start_index
        while i < len(words) and filled_spaces + len(words[i]) + 1 <= maxWidth + 1: 
            filled_spaces += len(words[i]) + 1
            end_index += 1
            i += 1
        return end_index
    
    def add_space(self, start_index, end_index, maxWidth, words):
        
        if start_index == end_index:
            return words[start_index] + ' ' * (maxWidth - len(words[start_index]))
        
        if end_index == len(words) - 1:
            word_space_string = ' '.join(words[start_index: end_index + 1])
            return word_space_string + ' ' * (maxWidth - len(word_space_string))
        
        word_space_list = words[start_index: end_index + 1]
        space_filled_by_words = 0
        for word in word_space_list:
            space_filled_by_words += len(word)
            
        total_width = space_filled_by_words
        while total_width < maxWidth:
            for i in range(0, len(word_space_list) - 1):
                word_space_list[i] += ' ' 
                #print(word_space_list)
                total_width += 1
                if total_width == maxWidth:
                    return ''.join(word_space_list)
        
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justified_string_list = []
        
        start_index = 0
        while start_index < len(words):
            #print('start', start_index)
            end_index = self.add_words(start_index, maxWidth, words)
            justified_string_list.append(self.add_space(start_index, end_index, maxWidth, words))
            start_index = end_index + 1
            
        return justified_string_list
            