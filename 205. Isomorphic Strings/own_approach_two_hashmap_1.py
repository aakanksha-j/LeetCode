class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # own approach - two hashmap (dictionary)

        # create two dictionaries eg. 'poo'{'p':1, 'o':2}
        # compare their length, compare the location of indices of each character

        # time: O(N) - len(string s or t)
        # space: O(N) - for dictionary

        dic_s = {ch: [] for ch in s}
        for i, ch in enumerate(s):
            dic_s[ch].append(i)

        dic_t = {ch: [] for ch in t}
        for i, ch in enumerate(t):
            dic_t[ch].append(i)

        if len(dic_s) == len(dic_t):
            found = 0
            for key1, key2 in zip(dic_s, dic_t):
                #print(key1, key2)
                if len(dic_s[key1]) == len(dic_t[key2]):
                    for value1, value2 in zip(dic_s[key1], dic_t[key2]):
                        if value1 != value2:
                            return False
                    found += 1
        else: # length of dictionaries not equal
            return False

        if found == len(dic_s):
            return True
        else:
            return False
