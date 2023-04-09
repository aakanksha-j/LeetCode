"""
243. Shortest Word Distance
Easy

1201

104

Add to List

Share
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
 

Constraints:

2 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
"""

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minimum_distance = len(wordsDict)
        word_1_index, word_2_index = -1, -1
        for index in range(len(wordsDict)):
            if wordsDict[index] == word1:
                word_1_index = index
                #print('w1', word_1_index)
                if word_2_index != -1:
                    minimum_distance = min((word_1_index - word_2_index), minimum_distance)
            if wordsDict[index] == word2:
                word_2_index = index
                #print('w2', word_2_index)
                if word_1_index != -1 and word1 != word2:
                    minimum_distance = min((word_2_index - word_1_index), minimum_distance)
        return minimum_distance
    
# O(n) time
# O(1) space

# 2 words are unique word1 != word2