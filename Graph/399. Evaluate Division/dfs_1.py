"""
399. Evaluate Division
Medium
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        pair_dic = {(equation[0], equation[1]): value for equation, value in zip(equations, values)}
        
        adj_list = {}
        for s1, s2 in equations:
            if s1 in adj_list:
                adj_list[s1].append(s2)
            else:
                adj_list[s1] = [s2]
            if s2 in adj_list:
                adj_list[s2].append(s1)
            else:
                adj_list[s2] = [s1]
        # print(adj_list)
        def calculate(d1, d2):
            # print(d1, d2)
            if (d1, d2) in pair_dic:
                return pair_dic[(d1, d2)]
            elif (d2, d1) in pair_dic:
                return 1/pair_dic[(d2, d1)]
            return 'not found'   
        output = []
        for idx, query in enumerate(queries):
            d1, d2 = query
            if d1 not in adj_list or d2 not in adj_list:
                output.append(-1.0)
                continue
            if d1 == d2:
                output.append(1.0)
                continue
            cache = calculate(d1, d2) 
            if cache != 'not found':
                # print(cache, pair_dic[(d2,d1)])
                output.append(cache)
                continue
            stack = [(d1, [d1])]
            visited = set()
            visited.add(d1) # 'aaa' saved as 'a' if visited = set(d1) is written
            while stack:
                node, path = stack.pop()
                # print(node, path)
                for nei in adj_list[node]:
                    # print(stack, visited, nei)
                    if nei == d2:
                        path.append(nei)
                        temp = 1.0
                        for i in range(len(path)-1):
                            temp *= calculate(path[i], path[i + 1])
                        output.append(temp)
                        stack = []
                        visited = set()
                        break
                    else:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append((nei, path + [nei]))
                            
            # print(idx, d1, d2, output)
            if len(output) < idx+1:
                output.append(-1.0)
        return output
            
"""I am not clear about time and space complexity. My guess:
time - O((N+E). no. of queries)
space - O(N) for adj list, tuple dictionary

Use an adj list to store nodes and edges.
Use a dictionary with tuple to store values between two nodes.
Use a helper function to return value of ratio or its inverse.
Use dfs to find if connections.

test cases:

one or both strings do not exist in input list (eg. input a,b:4, query: c/d)
both point to same node (query: a/a)
direct ratio available (input a/b:4, query: b/a)
will have to traverse entire graph to find connection (input a/b:2, c/d:4, b/c: 3, query: d/a)
both nodes exist but are not connected (input a/b:4, c/d:3, query: a/d)"""