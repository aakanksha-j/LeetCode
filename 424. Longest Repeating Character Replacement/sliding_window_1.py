class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window using dic for counter

        # time: O(n)
        # space: O(26) ~ constant

        count_dic = {} # can use collections.counter() as well
        start = max_count = 0

        for end in range(len(s)):
            count_dic[s[end]] = count_dic.get(s[end], 0) + 1
            max_count = max(count_dic[s[end]], max_count)

            if end - start + 1 > max_count + k:
                count_dic[s[start]] -= 1 # since our window shifts, we subtract
                # the character at start since it will no longer be in new window
                start += 1

        return len(s) - start # end - start + 1 since len(s), end + 1 gone

#https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91271/Java-12-lines-O(n)-sliding-window-solution-with-explanation
#https://leetcode.com/problems/longest-repeating-character-replacement/discuss/278271/JavaC%2B%2BPython-Sliding-Window-just-O(n)
#https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91301/Awesome-python-solution
