"""
245. Shortest Word Distance III
Medium

470

98

Add to List

Share
Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between the occurrence of these two words in the list.

Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.

 

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
Output: 3
 

Constraints:

1 <= wordsDict.length <= 105
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict."""

class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        n = len(words)
        minimum = n
        w1 = -1
        w2 = -1
        for i in range(n):
            if words[i] == word1:
                w1 = i
                if w2 != -1:
                    minimum = min(w1-w2, minimum)
            if words[i] == word2:
                w2 = i
                if w1 != -1 and w1 != w2:
                    minimum = min(w2-w1, minimum)
        return minimum
    
# O(n) time
# O(1) space

# https://leetcode.com/problems/shortest-word-distance-iii/discuss/165248/Python-solution