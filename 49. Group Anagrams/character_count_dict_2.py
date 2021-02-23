from collections import defaultdict
class Solution:
    """Approach 2: https://leetcode.com/problems/group-anagrams/solution/
                   Idea is to use a counter instead of sort or costly prime
                   multiplication. Hash construction is constant time and
                   does not change with input size, O(26).
       Time complexity: O(NK), where N is the length of strs, and K is the
                         maximum length of a string in strs. Counting each string
                         is linear in the size of the string, and we count every string.
       Space complexity: O(NK), the total information content stored in ans.
       Runtime: 116 ms
       Memory: 19.2 MB
    """
    def groupAnagrams(self, strs):
        cache = {}
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            cache[tuple(count)] = cache.get(tuple(count), []) + [word]
            print(cache[tuple(count)])
        return list(cache.values())

def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    s=Solution()
    print(s.groupAnagrams(strs))
    strs = [""]
    print(s.groupAnagrams(strs))
    strs = ["a"]
    print(s.groupAnagrams(strs))

if __name__ == '__main__':
    main()

"""cache = defaultdict(list)
for word in strs:
    count = [0] * 26
    for ch in word:
        count[ord(ch) - ord('a')] += 1
    cache[tuple(count)].append(word)
    print(cache[tuple(count)])
return list(cache.values())"""
