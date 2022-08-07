class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # bottom up dp O(1) space iterative

        # for 'a', we calculate how many nodes produce 'a' in previous level.

        # time: O(N) - N is input length n. Iterating from 1 to n will take O(N) time.
        # space: O(1) - we only store data of i-1th element in vowel variables

        # leetcode solution bottom up dp optimized space and https://leetcode.com/problems/count-vowels-permutation/discuss/398286/Simple-Python-(With-Diagram)

        a = e = i = o = u = 1

        for _ in range(1, n):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o

        return (a + e + i + o + u) % (10**9 + 7)



        
