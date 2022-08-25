class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/slidingwindowtechnique

        # sliding window algorithm using 2 hashmaps

        minLen = math.inf
        left, right = 0, 0
        needs = {ch: 0 for ch in t}
        for ch in t:
            needs[ch] += 1
        match, window = 0, {}

        while right < len(s):
            ch1 = s[right]
            if ch1 in needs:
                window[ch1] = window.get(ch1, 0) + 1
                if window[ch1] == needs[ch1]:
                    match += 1
            right += 1

            while match == len(needs):
                if right - left < minLen: # right - left + 1 not needed becouse right += 1 done above
                    start = left
                    minLen = right - left
                ch2 = s[left]
                if ch2 in needs:
                    window[ch2] -= 1
                    if window[ch2] < needs[ch2]:
                        match -= 1
                left += 1

        #print(window, needs, minLen, start)
        return '' if minLen == math.inf else s[start: start + minLen]
        
