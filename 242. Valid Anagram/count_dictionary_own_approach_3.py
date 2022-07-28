class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # own approach - count dictionary

        dic = {ch: 0 for ch in s}
        for ch in s:
            dic[ch] += 1

        for ch in t:
            if ch in dic:
                if dic[ch] > 0:
                    dic[ch] -= 1
                else:
                    return False
            else:
                return False

        for ch in dic:
            if dic[ch] != 0:
                return False

        return True
        
