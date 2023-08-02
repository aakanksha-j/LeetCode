"""
1128. Number of Equivalent Domino Pairs
Easy
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
 

Constraints:

1 <= dominoes.length <= 4 * 104
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9
"""
import collections
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = collections.defaultdict(int)
        for domino in dominoes:
            counter[tuple(sorted(domino))] +=1
        # if v =1, then v(v-1)//2 is 0  else is v choose 2.
        return sum([v*(v-1)//2 for v in counter.values()])

# time O(N)
# space O(N)

from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dictionary = collections.Counter()
        for domino in dominoes:
            dictionary[tuple(sorted(domino))] += 1
        output = 0
        print(dictionary)
        for val in dictionary.values():
            output += val * (val - 1) // 2
                
        return output
        