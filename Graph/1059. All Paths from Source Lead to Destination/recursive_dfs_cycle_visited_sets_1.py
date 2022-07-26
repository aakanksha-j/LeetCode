class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # dfs recursive using cycle and visited sets -
        # neetcode solution in course schedule 2

        # Instead of color coded approach, I have used 2 sets - cycle and
        # visited. Since there are states possible for every node: 'not visited'
        # , 'visiting' and 'visited', we need two sets.

        # time: O(V+E) - V: vertices, E: edges, we iterate through each node
        #       and each vertex in the graph only once
        # space: ~O(E) = O(V+E) - space occupied by adjacency list (E),
        #        recursive call stack (E).

        # build adjacency list
		adj_list = {src: [] for src, dst in edges}
        for src, dst in edges:
            adj_list[src].append(dst)

		cycle, visited = set(), set()

        def dfs(vertex):
			# 3 base cases
            if vertex not in adj_list: # end node with no leaves, not present as key in adj list
                return vertex == destination
            if vertex in cycle:
                return False
            if vertex in visited:
                return True

            cycle.add(vertex)
            for node in adj_list[vertex]:
                if not dfs(node):
                    return False
            cycle.remove(vertex)
            visited.add(vertex)
            return True

        return dfs(source)
