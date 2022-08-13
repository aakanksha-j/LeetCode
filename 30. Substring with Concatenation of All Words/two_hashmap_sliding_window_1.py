from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # two hash map - https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13658/Easy-Two-Map-Solution-(C%2B%2BJava)

        # time: O(N. numWords. wordLen) - N is length of string
        # space: O(N) - for wordBag dictionary, for seen dictionary

        wordBag = Counter(words) # count the freq of each word
        wordLen, numWords = len(words[0]), len(words)
        totalLen, res = wordLen*numWords, []
        for i in range(len(s) - totalLen + 1): # scan through s
            # for each i, determine if s[i: i+totalLen] is valid
            seen = defaultdict(int) # reset for each i
            for j in range(i, i + totalLen, wordLen):
                currWord = s[j: j + wordLen]
                if currWord in wordBag:
                    seen[currWord] += 1
                    if seen[currWord] > wordBag[currWord]:
                        break
                else: # if not in wordBag
                    break
            if seen == wordBag:
                res.append(i) # store result
        return res
