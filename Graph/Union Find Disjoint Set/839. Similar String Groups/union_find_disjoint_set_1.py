"""
839. Similar String Groups
Hard
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

 

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1
 

Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.

"""

# Union Find method from Graph Explore card
# time O(n^2. m) where n is # of words and m is length of string
# space O(n)

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
       
	   # disjoint set
        root = [i for i in range(len(strs))]
        rank = [1] * len(strs)
        
        def find(vertex):
            x = vertex
            # instead of recursion, while loop for path compression
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x

        def union(x, y): 
            rootX, rootY = find(x), find(y)
            # no union performed, therefore no increase in rank of parent
            if rootX == rootY:
                return 0
            # union by rank
            if rank[rootX] > rank[rootY]:
                root[rootY] = rootX
                rank[rootX] += rank[rootY]
            else:
                root[rootX] = rootY
                rank[rootY] += rank[rootX]
            # union performed, so return 1
            return 1               
            
        
		
		# check if similar strings   
        def are_similar(s1, s2):
            if s1 == s2: return True

            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
         
            return True if count <= 2 else False
            
    
        # for loop needed so n^2 time, need to compare every pair not just adjacent pairs
        output = len(strs)
        for i, vertex1 in enumerate(strs[:-1]):
            for j, vertex2 in enumerate(strs[i+1:], i+1):
                if are_similar(vertex1, vertex2):
                    output -= union(i, j)
      
        return output