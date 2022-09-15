class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # neetcode solution

        # valid tree definition:
        # 1. no cycles detected
        # 2. all nodes are connected

        # edge case: no nodes means, empty tree, which is valid
        if not n:
            return True

        # build adjacency list
        adj = { e: [] for e in range(n) }
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        # dfs to check if there is a cycle
        visit = set()
        def dfs(curr, prev):

            # current edge in visited set means there is a cycle
            if curr in visit:
                return False

            visit.add(curr)

            for edge in adj[curr]:
                # if one of curr node's edge is equal to prev means visiting previous node and not a cycle
                if edge == prev:
                    continue
                # pass curr node as previous for the edge and check for cycle
                if not dfs(edge, curr):
                    return False

            return True

        # dfs condition should come before all nodes connected condition, otherwise false output
        return dfs(0, -1) and len(visit) == n 
