"""
1065. Index Pairs of a String
Easy
Given a string text and an array of strings words, return an array of all index pairs [i, j] so that the substring text[i...j] is in words.

Return the pairs [i, j] in sorted order (i.e., sort them by their first coordinate, and in case of ties sort them by their second coordinate).

 

Example 1:

Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13],[10,17]]
Example 2:

Input: text = "ababa", words = ["aba","ab"]
Output: [[0,1],[0,2],[2,3],[2,4]]
Explanation: Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].
 

Constraints:

1 <= text.length <= 100
1 <= words.length <= 20
1 <= words[i].length <= 50
text and words[i] consist of lowercase English letters.
All the strings of words are unique."""

# own approach
from typing import List


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        output = []
        
        for word in words:
            i = text.find(word)
            if i == -1:
                continue
            else:
                while i != -1:
                    output.append([i, i + len(word) - 1])
                    i = text.find(word, i + 1)
                    if i == -1:
                        break

        output.sort(key = lambda x: (x[0], x[1]))
        return output
    
"""Approach:

Run for loop on every word to find its locations
Inside for loop, find the word,
2.1 if not found, go to next word
2.2 if found, using while loop, append locations to output, find the next position by searching from next index
sort output based on first coordinate, and in case of tie, second coordinate, return output
time: O(n.m.m) - n: length of words, m: lenth of text string
space: O(1)
I am not sure about the time and space complexity.
"""

# using hashset
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        output = []
        words = set(words)
        for i in range(len(text)):
            for j in range(i, len(text)):
                if text[i: j + 1] in words:
                    output.append([i, j])
        return output
    
# time O(n.s + m^3) - n: length of words, m: length of text, s: length of one word on average
# space: O(n.s) - for hashset                
                
                