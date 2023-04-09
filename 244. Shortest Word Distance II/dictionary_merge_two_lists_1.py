class WordDistance:

# time O(m+n) length of list1 - m, length of list2 - n
# space O(N) -space for dictionary

# make sure to declare variable for words list length to assign it to min_distance

    def __init__(self, wordsDict: List[str]):
        self.words_list_length = len(wordsDict)
        self.dictionary = {word: [] for word in wordsDict}
        for index, word in enumerate(wordsDict):
            self.dictionary[word].append(index)
        

    def shortest(self, word1: str, word2: str) -> int:
        index_list_1 = self.dictionary[word1]
        index_list_2 = self.dictionary[word2]
        
        min_distance = self.words_list_length
        
        i1, i2 = 0, 0 
        while i1 < len(index_list_1) and i2 < len(index_list_2):
            min_distance = min(min_distance, abs(index_list_1[i1]-index_list_2[i2]))
            if min_distance == 1:
                return 1
            if index_list_1[i1] < index_list_2[i2]:
                i1 += 1
            else:
                i2 += 1
     
        return min_distance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

# https://leetcode.com/problems/shortest-word-distance-ii/discuss/67075/Python-O(m%2Bn)-time-solution.
