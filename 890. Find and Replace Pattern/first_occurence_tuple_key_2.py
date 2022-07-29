class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # using first occurence index of ch as list
        # convert the list to tuple
        # use tuple as key for dictionary
        # add all the words with same key as values to dictionary

        # eg. 'abb', 'foo' have key: (0,1,1) and values: ['abb', 'foo']

        word_dic = {}

        pattern_key = []
        for ch in pattern:
            pattern_key.append(pattern.find(ch))
        pattern_key = tuple(pattern_key)
        word_dic[pattern_key] = [pattern]

        for word in words:
            key = tuple([word.find(ch) for ch in word])
            word_dic[key] = word_dic.get(key, []) + [word]

        if len(word_dic[pattern_key]) > 1:
            return word_dic[pattern_key][1:]
        else:
            return []

            
